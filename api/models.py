from django.db import models


class Organization(models.Model):
    abbr = models.TextField()
    is_active = models.BooleanField(default=True)
    
    
class Audience(models.Model):
    organization = models.ForeignKey("api.Organization", on_delete=models.CASCADE)
    member_sn = models.TextField()
    name = models.TextField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "member_sn"],
                name="audience_unique_member_sn",
            ),
        ]
    
    
class Tag(models.Model):
    organization = models.ForeignKey("api.Organization", on_delete=models.CASCADE)
    name = models.TextField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "name"],
                name="tag_unique_name",
            ),
        ]
        
        
class Log(models.Model):
    organization = models.ForeignKey("api.Organization", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    data = models.JSONField(default=dict)
    
    
class Report(models.Model):
    organization = models.ForeignKey("api.Organization", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    
    
class TagReport(Report):
    tag = models.ForeignKey("api.Tag", on_delete=models.CASCADE)