from turtle import title


# 5강 데이터 관리
# class와 인스턴스를 이용해서 데이터를 저장할 때 장점

class Review:
    title = ''
    content = ''
    user = ''

    def __init__(self, content=content, title=title, user=user): # content=content: 키=값(변수)
        self.content = content
        self.title = title
        self.user = user

review1 = Review(title="타이틀1", content="영화가 재밌었다", user="poco")
review2 = Review(title="타이틀2", content="영화가 와구와구", user="pie")
review3 = Review(title="타이틀3", content="영화가 와랄랄라", user="dorimi")
review4 = Review(title="타이틀4", content="영화가 우적우적", user="ingreum")

print(review1.title, review1.content, review1.user)

# 파일을 실행할 때만 존재, 다른 곳에 보관(DB)하는 것이 중요