# n = number of movies chef friend has
# x = space remaining in chef harddisk
# s = space_required
# r = rating
movie_info = []


def check(ele):
    return ele[0] <= x


for _ in range(int(input())):
    n, x = [int(val) for val in input().split()]
    for i in range(n):
        # taking each movie size and imdb rating
        s, r = [int(val) for val in input().split()]
        movie_info.append((s, r))
        # truncate movies whose size is greater than chef's
    new_movie_info = list(filter(check, movie_info))
    new_movie_info.sort(key=lambda x: x[1],reverse=True)
    print(new_movie_info[0][1])
    movie_info.clear()
    new_movie_info.clear()

