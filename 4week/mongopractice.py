from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.dbsparta

def question1():
    # 어벤져스: 엔드게임 의 평점을 가져오자
    movie = db.movies.find_one(
        {"title": "어벤져스: 엔드게임"}
    )
    print(movie["star"])

def question2():
    # 어벤져스: 엔드게임 평점이 같은 영화의 제목 가져오기
    avengers = db.movies.find_one({"title": "어벤져스: 엔드게임"})
    avengers_star = avengers["star"]

    movies = list(db.movies.find({"star": avengers_star}))
    for movie in movies:
        print(movie["title"])

def question3():
    # 어벤져스: 엔드게임과 평점이 같은 영화의 평점을 0으로 만들기
    avengers = db.movies.find_one({"title": "어벤져스: 엔드게임"})
    avengers_star = avengers["star"]
    print(avengers_star)
    # 평점 같은 영화 조회 후 수정
    db.movies.update_many(
        {"star": avengers_star}, {"$set": {"star": 0}}
    )

if __name__ == "__main__":
    # question1()
    # question2()
    question3()