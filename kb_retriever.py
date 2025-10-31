from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SmartKBRetriever:
    """Enhanced KB retrieval using TF-IDF and cosine similarity"""
    
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.vectorizers = {}
        self.article_vectors = {}
        self._build_indexes()
    
    def _build_indexes(self):
        """Build TF-IDF indexes for each persona"""
        for persona, articles in self.knowledge_base.items():
            if not articles:
                continue
            
            # Combine title, content, and keywords for better matching
            documents = []
            for article in articles:
                doc_text = f"{article['title']} {article['content']} {' '.join(article['keywords'])}"
                documents.append(doc_text)
            
            # Create TF-IDF vectorizer
            vectorizer = TfidfVectorizer(
                stop_words='english',
                ngram_range=(1, 2),  # Use unigrams and bigrams
                max_features=100
            )
            
            # Fit and transform documents
            vectors = vectorizer.fit_transform(documents)
            
            self.vectorizers[persona] = vectorizer
            self.article_vectors[persona] = vectors
    
    def retrieve(self, persona, query, conversation_history=None, top_k=3):
        """
        Retrieve relevant KB articles using TF-IDF similarity
        
        Args:
            persona: Customer persona type
            query: Current user query
            conversation_history: Previous conversation for context
            top_k: Number of articles to return
        """
        if persona not in self.vectorizers:
            return []
        
        # Enhance query with conversation context
        enhanced_query = query
        if conversation_history and len(conversation_history) > 0:
            # Add last 2 user messages for context
            recent_messages = [
                msg['content'] for msg in conversation_history[-4:]
                if msg['role'] == 'user'
            ][-2:]
            enhanced_query = f"{query} {' '.join(recent_messages)}"
        
        # Transform query to vector
        vectorizer = self.vectorizers[persona]
        query_vector = vectorizer.transform([enhanced_query])
        
        # Calculate cosine similarity with all articles
        similarities = cosine_similarity(
            query_vector,
            self.article_vectors[persona]
        ).flatten()
        
        # Get top-k articles
        articles = self.knowledge_base[persona]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Filter out articles with very low similarity (< 0.1)
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # Threshold for relevance
                article = articles[idx].copy()
                article['relevance_score'] = float(similarities[idx])
                results.append(article)
        
        return results
    
    def get_keyword_matches(self, persona, query):
        """
        Fallback: Simple keyword matching (used as backup)
        """
        kb_articles = self.knowledge_base.get(persona, [])
        message_lower = query.lower()
        
        scored_articles = []
        for article in kb_articles:
            score = sum(1 for keyword in article["keywords"] if keyword in message_lower)
            if score > 0:
                scored_articles.append((score, article))
        
        scored_articles.sort(reverse=True, key=lambda x: x[0])
        return [article for _, article in scored_articles[:3]]