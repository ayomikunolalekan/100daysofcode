print("What generation do you belong to 🤔?")
print()
birthYear = int(input("Hello!! What year were you born?: "))

if birthYear >= 1925 and birthYear <= 1946:
  print("You belong to the generation 'Traditionalists' ✨✨. You really must have a wealth of knowledge and experience.")
elif birthYear >= 1947 and birthYear <= 1964:
  print("You belong to the generation 'Baby Boomers'. I guess there were a lot of booming babies that period 😅😅")
elif birthYear >= 1965 and birthYear <= 1981:
  print("You belong to 'Generation X'. I guess we can call you guys X-men or X-women 😅😅")
elif birthYear >= 1982 and birthYear <= 1995:
  print("You belong to the 'Millenials' generation. Pleased to make your acquaintance 😊")
elif birthYear >= 1996 and birthYear <= 2015:
  print("My generation. Congratulations, you belong to 'Generation Z'. Really nice to meet a fellow Gen Z 😊")
else:
  print("Hey, I'm really sorry I couldn't add your generation. I wasn't able to find the accurate start and end date for it. Maybe next time but anyways nice to meet you 😊")