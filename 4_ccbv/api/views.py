from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from api.views_util import obj_to_post
from model.models import Verification


class ApiPostLV(BaseListView):
    model = Verification

    # noinspection PyMethodMayBeStatic
    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postList = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=postList, safe=False, status=200)


class ApiPostDV(BaseDetailView):
    model = Verification

    # noinspection PyMethodMayBeStatic
    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        return JsonResponse(data=post, safe=True, status=200)