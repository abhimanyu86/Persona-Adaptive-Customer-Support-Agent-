import time
from collections import defaultdict
from datetime import datetime

class MetricsTracker:
    """Track agent performance metrics"""
    
    def __init__(self):
        self.metrics = {
            "total_requests": 0,
            "persona_detections": defaultdict(int),
            "kb_hits": 0,
            "kb_misses": 0,
            "escalations": 0,
            "avg_response_time": 0,
            "avg_confidence": 0,
            "sentiment_distribution": defaultdict(int),
            "urgency_distribution": defaultdict(int),
        }
        self.response_times = []
        self.confidence_scores = []
    
    def record_request(self, persona, kb_articles, confidence, response_time, escalated, sentiment, urgency):
        """Record metrics for a single request"""
        self.metrics["total_requests"] += 1
        self.metrics["persona_detections"][persona] += 1
        self.metrics["sentiment_distribution"][sentiment] += 1
        self.metrics["urgency_distribution"][urgency] += 1
        
        # KB metrics
        if kb_articles:
            self.metrics["kb_hits"] += 1
        else:
            self.metrics["kb_misses"] += 1
        
        # Escalation
        if escalated:
            self.metrics["escalations"] += 1
        
        # Track response time
        self.response_times.append(response_time)
        self.metrics["avg_response_time"] = sum(self.response_times) / len(self.response_times)
        
        # Track confidence
        self.confidence_scores.append(confidence)
        self.metrics["avg_confidence"] = sum(self.confidence_scores) / len(self.confidence_scores)
    
    def get_summary(self):
        """Get metrics summary"""
        total = self.metrics["total_requests"]
        if total == 0:
            return {"message": "No requests yet"}
        
        kb_hit_rate = (self.metrics["kb_hits"] / total) * 100 if total > 0 else 0
        escalation_rate = (self.metrics["escalations"] / total) * 100 if total > 0 else 0
        
        return {
            "total_requests": total,
            "persona_distribution": dict(self.metrics["persona_detections"]),
            "kb_hit_rate": f"{kb_hit_rate:.1f}%",
            "escalation_rate": f"{escalation_rate:.1f}%",
            "avg_response_time": f"{self.metrics['avg_response_time']:.2f}s",
            "avg_confidence": f"{self.metrics['avg_confidence']:.2f}",
            "sentiment_distribution": dict(self.metrics["sentiment_distribution"]),
            "urgency_distribution": dict(self.metrics["urgency_distribution"]),
        }
    
    def get_detailed_metrics(self):
        """Get all metrics"""
        return {
            **self.metrics,
            "summary": self.get_summary()
        }