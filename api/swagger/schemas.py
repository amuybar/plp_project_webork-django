from drf_yasg import openapi # type: ignore

get_started_schema = {
    'list': openapi.Schema(
        title="GetStarted List",
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'phone': openapi.Schema(type=openapi.TYPE_STRING),
            'country': openapi.Schema(type=openapi.TYPE_STRING),
            'message': openapi.Schema(type=openapi.TYPE_STRING),
            'date_added': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        }
    ),
    'create': openapi.Schema(
        title="Create GetStarted",
        type=openapi.TYPE_OBJECT,
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'phone': openapi.Schema(type=openapi.TYPE_STRING),
            'country': openapi.Schema(type=openapi.TYPE_STRING),
            'message': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
}

bid_service_schema = {
    'list': openapi.Schema(
        title="BidService List",
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'price': openapi.Schema(type=openapi.TYPE_NUMBER),
            'date_added': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        }
    ),
    'create': openapi.Schema(
        title="Create BidService",
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'price': openapi.Schema(type=openapi.TYPE_NUMBER),
        }
    ),
}

newsletter_schema = {
    'list': openapi.Schema(
        title="Newsletter List",
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'date_added': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        }
    ),
    'create': openapi.Schema(
        title="Create Newsletter",
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
}

messages_schema = {
    'list': openapi.Schema(
        title="Messages List",
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'subject': openapi.Schema(type=openapi.TYPE_STRING),
            'content': openapi.Schema(type=openapi.TYPE_STRING),
            'date_sent': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        }
    ),
    'create': openapi.Schema(
        title="Create Message",
        type=openapi.TYPE_OBJECT,
        properties={
            'subject': openapi.Schema(type=openapi.TYPE_STRING),
            'content': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
}

services_schema = {
    'list': openapi.Schema(
        title="Services List",
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'image': openapi.Schema(type=openapi.TYPE_STRING),
            'quotation': openapi.Schema(type=openapi.TYPE_STRING),
            'expected_time': openapi.Schema(type=openapi.TYPE_STRING),
            'colaboration': openapi.Schema(type=openapi.TYPE_STRING),
            'date_added': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            }
        ),
    'create': openapi.Schema(
        title="Create Services",
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'image': openapi.Schema(type=openapi.TYPE_STRING),
            'quotation': openapi.Schema(type=openapi.TYPE_STRING),
            'expected_time': openapi.Schema(type=openapi.TYPE_STRING),
            'colaboration': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
    }

blogs_schema = {
    'list': openapi.Schema(
        title="Blogs List",
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'image': openapi.Schema(type=openapi.TYPE_STRING),
            'date_added': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            }
        ),
    'create': openapi.Schema(
        title="Create Blogs",
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'image': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
    }

