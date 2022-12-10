from django.urls import path
from . import views


urlpatterns = [
    path('all/',views.getTbNewsAll,name='newsAll'),
    path('press/<str:press>/',views.getNewsPerPress, name='newsPress'),
    path('mCategory/<str:maincategory>/',views.getNewsPerMCategory, name='newsMCategory'),
    path('up-to-date/recomm_news/<int:newsid>/',views.getNewsRecommend,name='newsRecommend'),
    path('<int:newsid>',views.getNews,name='news'),
]


# - /news/all/ : 모든 카테고리의 최신뉴스를 가지고 와야 한다.
# - /news/press/"언론사명": 언론사별 최신뉴스를 가지고 와야한다.
# - /news/mCategory/"카테고리" : 카테고리별 최신뉴스를 가지고 와야 한다.

# - /news/up-to-date/recomm_news : 사용자가 기사 선택 후 그 기사와 유사도가 높은 기사를 추천 해와야 한다.
# - /news/user/recommend_news : 사용자가 로그인 시 그 사용자의 맞는 추천 기사를 가지고 와야 한다.