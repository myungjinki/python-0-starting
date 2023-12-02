ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list는 mutable iterable이라 값을 바꿀 수 있습니다.
ft_list[1] = "World!"

# tuple은 immutable iterable이라 값을 바꿀 수 없습니다.
ft_tuple = ("Hello", "Korea!")

# set은 Set Types입니다. 중복된 값을 허용하지 않습니다.
ft_set.remove("tutu!")
ft_set.add("Seoul!")

# dict는 Mapping Types이며 key는 hashable object이고 value는 arbitrary object입니다.
ft_dict["Hello"] = "42Seoul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
