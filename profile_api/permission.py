from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own permission"""
    
    def has_object_permission(self, request, view, obj):
        """Check user trying to edit there own profile"""
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
            