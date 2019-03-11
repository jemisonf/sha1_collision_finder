import hashlib
import random
import string

HASH_COLLISION_SIZE = 10

def get_rand_byte_string(size):
    letters = string.ascii_lowercase
    return str.encode(''.join(random.choice(letters) for i in range(size)))

def file_to_string(filename):
    with open(filename, 'rb') as f:
        string = f.read()
    return string

def write_string(filename, string):
    with open(filename, 'wb') as f:
        f.write(string)
    


def find_collisions(cat_file, dog_file):
    catstr = file_to_string(cat_file)
    dogstr = file_to_string(dog_file)
    cat_hashes = {}
    dog_hashes = {}
    count = 0
    while(True):
        count += 1
        rand_catstr = catstr + get_rand_byte_string(10000)
        rand_dogstr = dogstr + get_rand_byte_string(10000)
        cat_hash = hashlib.sha1(rand_catstr).hexdigest()[:HASH_COLLISION_SIZE]
        dog_hash = hashlib.sha1(rand_dogstr).hexdigest()[:HASH_COLLISION_SIZE]
        cat_hashes[cat_hash] = rand_catstr
        dog_hashes[dog_hash] = rand_dogstr
        if (dog_hash in cat_hashes):
            return (cat_hashes[dog_hash], rand_dogstr, count)
        elif (cat_hash in dog_hashes):
            return (rand_catstr, dog_hashes[cat_hash], count)

cat_string, dog_string, count = find_collisions("cat.jpg", "dog.jpg")

print(f"Found collision in {count} attempts")
write_string("cat_collision.jpg", cat_string)
write_string("dog_collision.jpg", dog_string)
