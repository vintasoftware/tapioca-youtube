# coding: utf-8

RESOURCE_MAPPING = {
    'activities': {
        'resource': 'activities',
        'docs': 'https://developers.google.com/youtube/v3/docs/activities',
        'methods': ['GET', 'POST']
    },
    'captions': {
        'resource': 'captions',
        'docs': 'https://developers.google.com/youtube/v3/docs/captions',
        'methods': ['GET', 'POST', 'PUT', 'DELETE']
    },
    'caption': {
        'resource': 'captions/{id}',
        'docs': 'https://developers.google.com/youtube/v3/docs/captions/download',
        'methods': ['GET']
    },
    'channel_banners': {
        'resource': 'channelBanners/insert',
        'docs': 'https://developers.google.com/youtube/v3/docs/channelBanners/insert',
        'methods': ['POST']
    },
    'channels': {
        'resource': 'channels',
        'docs': 'https://developers.google.com/youtube/v3/docs/channels',
        'methods': ['GET', 'PUT']
    },
    'channel_sections': {
        'resource': 'channelSections',
        'docs': 'https://developers.google.com/youtube/v3/docs/channelSections',
        'methods': ['GET', 'POST', 'PUT', 'DELETE']
    },
    'comments': {
        'resource': 'comments',
        'docs': 'https://developers.google.com/youtube/v3/docs/comments',
        'methods': ['GET', 'POST', 'PUT', 'DELETE']
    },
    'comments_mark_as_spam': {
        'resource': 'comments/markAsSpam',
        'docs': 'https://developers.google.com/youtube/v3/docs/comments',
        'methods': ['POST']
    },
    'comments_set_moderation_status': {
        'resource': 'comments/setModerationStatus',
        'docs': 'https://developers.google.com/youtube/v3/docs/comments',
        'methods': ['POST']
    },
    'comment_threads': {
        'resource': 'commentThreads',
        'docs': 'https://developers.google.com/youtube/v3/docs/commentThreads',
        'methods': ['GET', 'POST', 'PUT',]
    },
    'guide_categories': {
        'resource': 'guideCategories',
        'docs': 'https://developers.google.com/youtube/v3/docs/guideCategories',
        'methods': ['GET']
    },
    'playlist_items': {
        'resource': 'playlistItems',
        'docs': 'https://developers.google.com/youtube/v3/docs/playlistItems',
        'methods': ['GET', 'POST', 'PUT', 'DELETE']
    },
    'playlists': {
        'resource': 'playlists',
        'docs': 'https://developers.google.com/youtube/v3/docs/playlists',
        'methods': ['GET', 'POST', 'PUT', 'DELETE']
    },
    'search': {
        'resource': 'search',
        'docs': 'https://developers.google.com/youtube/v3/docs/search',
        'methods': ['GET']
    },
    'subscriptions': {
        'resource': 'subscriptions',
        'docs': 'https://developers.google.com/youtube/v3/docs/subscriptions',
        'methods': ['GET', 'POST', 'DELETE']
    },
    'thumbnails': {
        'resource': 'thumbnails/set',
        'docs': 'https://developers.google.com/youtube/v3/docs/thumbnails',
        'methods': ['POST']
    },
    'video_abuse_report_reasons': {
        'resource': 'videoAbuseReportReasons',
        'docs': 'https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons',
        'methods': ['GET']
    },
    'video_categories': {
        'resource': 'videoCategories',
        'docs': 'https://developers.google.com/youtube/v3/docs/videoCategories',
        'methods': ['GET']
    },
    'videos': {
        'resource': 'videos',
        'docs': 'https://developers.google.com/youtube/v3/docs/videos',
        'methods': ['GET', 'POST', 'PUT', 'DELETE']
    },
    'videos_rate': {
        'resource': 'videos/rate',
        'docs': 'https://developers.google.com/youtube/v3/docs/videos/rate',
        'methods': ['POST']
    },
    'videos_get_rating': {
        'resource': 'videos/getRating',
        'docs': 'https://developers.google.com/youtube/v3/docs/videos/getRating',
        'methods': ['GET']
    },
    'watermarks_set': {
        'resource': 'watermarks/set',
        'docs': 'https://developers.google.com/youtube/v3/docs/watermarks/set',
        'methods': ['POST']
    },
    'watermarks_unset': {
        'resource': 'watermarks/unset',
        'docs': 'https://developers.google.com/youtube/v3/docs/watermarks/unset',
        'methods': ['POST']
    },
}
