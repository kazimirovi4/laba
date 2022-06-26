def zeros(n):
    return 0 if int(n//5) < 1 else int(n//5) + int(zeros(n//5))

if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
