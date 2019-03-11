import hashlib
import random
import string

HASH_COLLISION_SIZE = 2

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
        rand_catstr = get_rand_byte_string(100)
        rand_dogstr = get_rand_byte_string(100)
        cat_hash = hashlib.sha1(catstr + rand_catstr).hexdigest()[:HASH_COLLISION_SIZE]
        dog_hash = hashlib.sha1(catstr + rand_dogstr).hexdigest()[:HASH_COLLISION_SIZE]
        cat_hashes[cat_hash] = rand_catstr
        dog_hashes[dog_hash] = rand_dogstr
        if (cat_hash in dog_hashes):
            return (catstr + rand_catstr, dog_hashes[cat_hash], count)
        if (dog_hash in cat_hashes):
            return (catstr + cat_hashes[dog_hash], dogstr + rand_dogstr, count)

cat_string, dog_string, count = find_collisions("cat.jpg", "dog.jpg")

print(count)
write_string("cat_collision.jpg", cat_string)
write_string("dog_collision.jpg", dog_string)
