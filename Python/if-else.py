dish = input("enter the dish: ")
indian = ["chicken biryani","samosa","dosa sambar","jigarthanda"]
japanese = ["takoyaki","ramen","sushi","onigiri","mochi"]
italian = ["pizza","pasta","mac nd cheese","ice cream","matcha"]

if dish in indian:
    print("indian")
elif dish in japanese:
    print("japanese")
elif dish in italian:
    print("italian")
else:
    print("i have very little , idk which cuisine it belongs to...")