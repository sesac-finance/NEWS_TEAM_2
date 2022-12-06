from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)                       # 기사 id, PK
    domain_id = models.IntegerField()                                # 기사 플랫폼 id: 네이버 1 / 다음 2
    main_category = models.CharField(max_length=16, blank=True)      # 대분류
    sub_category = models.CharField(max_length=16, blank=True)       # 소분류
    writed_at = models.DateTimeField(blank=True, null=True)          # 기사 작성시간
    title = models.CharField(max_length=128, blank=True)             # 기사 제목
    content = models.TextField()                                     # 기사 본문
    url = models.CharField(max_length=255, blank=True)               # 기사 url
    photo_url = models.TextField(blank=True)                         # 사진 url
    writer = models.CharField(max_length=16, blank=True)             # 기자
    stickers = models.TextField(blank=True)                          # 기사에 대한 반응
    press = models.CharField(max_length=16, blank=True)              # 언론사

    def __str__(self): # 객체를 문자열로 바꾸어 어드민 페이지 및 대화식 프롬프트에서 객체의 표현을 확인할 수 있게 함
        return self.title

class Comment(models.Model):
    c_id = models.IntegerField()                                     # 댓글 id
    news_id = models.ForeignKey(Article, on_delete=models.CASCADE)   # 기사 id, FK
    user_id = models.IntegerField()                                  # 댓글 작성자 id
    c_writed_at = models.DateTimeField(blank=True, null=True)        # 댓글 작성시간
    c_content = models.TextField(blank=True)                         # 댓글 내용
    
    def __str__(self):
        return self.c_content