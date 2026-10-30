def get_ordered_comments_by_likes(comments : list) -> list:
    answer = []
    for comment in comments:
        answer.append(comment)
    answer.sort(key=lambda comment: -comment.like_count)
    return answer
