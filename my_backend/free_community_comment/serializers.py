from rest_framework import serializers

from free_community_comment.entity.models import FreeCommunityComment


class FreeCommunityCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeCommunityComment
        fields = ['commentId', 'free_community', 'content', 'nickname', 'parent', 'regDate', 'updDate']
        read_only_fields = ['commentId', 'regDate', 'updDate']