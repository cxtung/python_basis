def kttamgiac(a,b,c):
    if (a+b>c and a+c>b and b+c>a):
        if a==b==c :
            print('tam giác đều')
        elif a==b or b==c or c==a:
            print('tam giác cân')
        else:
            print(' tam giác thường')
    else:
        print('không phải tam giác')
kttamgiac(a,b,c)
test_case=[
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
for a, b, c in test_cases:
    result = kttamgiac(a, b, c)
    print(f"Tam giác có các cạnh ({a}, {b}, {c}): {result}")
