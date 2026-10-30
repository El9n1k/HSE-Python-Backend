def select_top_users_by_rate(users: list, top_size: int) -> list:
    answer = users[::]
    answer.sort(key=lambda user: user.rate)
    return answer[len(answer) - top_size:]
