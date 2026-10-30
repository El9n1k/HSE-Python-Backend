from models.user import User

def filter_comments_by_author(comments: list, author: User) -> list:
    answer = []
    id = author.id
    for comment in comments:
        if comment.author_id == id:
            answer.append(comment)
    return answer

