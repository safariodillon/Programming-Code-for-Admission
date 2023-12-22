#Here is the correct answer i have tried
#some problems found in this program are:
#idx += 1 line should be outside the if block, and second, the fruit_id should be compared with the idx after the return statement and the  the idx += 1 line is placed outside the if block, and the raise RuntimeError line is outside the loop, ensuring it is only raised if the loop completes without finding a match for the given fruit_id.
# You can copy this code to your personal pipeline project or execute it here.
def id_to_fruit(fruit_id: int, fruits: Set[str]) -> str:
    idx = 0
    for fruit in fruits:
        if fruit_id == idx:
            return fruit
        idx += 1
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")

name1 = id_to_fruit(1, {"apple", "orange", "melon", "kiwi", "strawberry"})
name3 = id_to_fruit(3, {"apple", "orange", "melon", "kiwi", "strawberry"})
name4 = id_to_fruit(4, {"apple", "orange", "melon", "kiwi", "strawberry"})

print(name1)  # Expected output: 'orange'
print(name3)  # Expected output: 'kiwi'
print(name4)  # Expected output: 'strawberry'
