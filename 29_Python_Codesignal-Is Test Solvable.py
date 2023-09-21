def solution(ids, k):
    def digitSum(id): return sum(int(x) for x in str(id))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
