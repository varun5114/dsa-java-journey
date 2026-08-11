# Google Preparation Master Notes

---

## 1. DSA Patterns
Concepts and patterns learned while solving problems.

### Array Pattern 1 — Hash Lookup
    Used when quick existence checking required.
    Data Structure: HashMap / HashSet
    Time Complexity Improvement: O(n²) → O(n)
    When to use:
When I need to check if a value already exists while traversing an array.

Core Idea:
Store previously seen elements in a HashMap or HashSet.

Steps:
1. Traverse the array once.
2. Before inserting element, check if the needed value exists.
3. If yes → answer found.
4. If no → store current element.
Example Problems:
Two Sum
Valid Anagram
Contains Duplicate

### HashSet
1. used for Fast lookup
2. unique Elements
3. duplicate deletion

### Running Minimum pattern
1. used to track minimum so far
2. calculate profit
3. update maximum profit

### Queue operations

enqueue
dequeue
peek
LIFO


### Pattern: Kadane’s Algorithm (Maximum Subarray)

When to use:
When the problem asks for maximum sum of a contiguous subarray.

Core Idea:
Keep track of running sum.
If the sum becomes negative, reset it.

Steps:
1. Traverse array.
2. Add current element to running sum.
3. Update maximum if needed.
4. If running sum < 0 → reset to 0.

Time Complexity:
O(n)

Example Problems:
Maximum Subarray
Maximum Sum Subarray

### Pattern: Two Pointer Technique

When to use:
When working with arrays or strings where two indices must move.

Types:
1. Slow + Fast pointer
2. Left + Right pointer

Core Idea:
One pointer reads data.
Another pointer modifies or tracks position.

Example Problems:
Remove Duplicates from Sorted Array
Move Zeroes
Two Sum (sorted version)

### Pattern: Frequency Counting
    Used for anagram, duplicates, character comparison.

### Pattern: Running Accumulation
    Maintain value while traversing.

### Linked list

Node 
head
tail
next

### reverse linked list
prev
current
next

### fast and slow pointer

slow+=1
fast+=2

### stack Notes

Monotonic stack
next greater element

LIFO


### Pattern: Sliding Window (Fixed Size)

Used when subarray of size k needed.

Sliding window used for:
substring
subarray
k size window
unique elements

Steps:
add element
check condition
shrink window
update result

Common mistakes:
i-k-1 error
remove wrong element
wrong order

### fast & slow pointer 
middle
cycle detection (aka floyds cycle detection algorithm)

### reverse linked list
prev
current
next

### linked list cycle
slow == fast




### Pattern: Two Pointer from both ends
Used when array sorted
Left and right move toward center

### PREFIX / SUFFIX PATTERNS
Pattern: Prefix Sum

Used when:
- need sum of subarray
- need fast range sum
- repeated sum queries
- subarray sum equals k

Idea:
prefix[i] = sum of elements from 0 to i

sum(l, r) =
prefix[r] - prefix[l-1]

Common problems:
- Subarray Sum Equals K
- Range sum queries
- Continuous subarray problems

Often used with:
HashMap

Prefix + HashMap → find previous sum quickly

Pattern: Suffix

Used when:
- need values from right side
- need product except self
- need future values

Idea:
suffix[i] = result from i to end

Used with prefix to avoid extra loops

Common problems:
- Product of Array Except Self
- Trapping Rain Water (later)
- prefix + suffix problems

Prefix + Suffix → avoid division / nested loops


Pattern: Prefix + HashMap

Used when:
- subarray sum = k
- need count of subarrays
- need previous sums

Idea:
currentSum += nums[i]

if (currentSum - k) exists in map
→ subarray found

Store:
map.put(sum, count)

Common problems:
- Subarray Sum Equals K
- Continuous subarray sum
- Count subarrays with sum

Always put 0 → 1 in map at start
eg:-map.put(0,1)

Common mistakes in prefix problems

- forgetting map.put(0,1)
- wrong order of update
- using i-1 incorrectly
- overflow sum
- not checking before adding

### Binary search Pattern

Used when sorted
low high mid
while <=

mid=left+(right-left)/2

mistakes:
low < high
wrong mid
infinite loop

### Binary search variations
first occurrence
last occurrence
insert position

### stack Pattern

LIFO
push pop peek

used for:
parentheses
undo
reverse
next greater

### Tree Basics
root
leaf
height
depth

### Maximum depth
max(left,right)+1

### Same tree
compare values
compare left
compare right

### queue notes
FIFO
implementation tricks(im comfortable with DFS now)



### Recursion 
Base case
Recursive call

### DFS
root
left
right

### Trees
root
leaf
height
depth

 1. Maximum Depth:
    return 1+Math.max(maxDepth(root.left),maxDepth(root.right))
 2. Same tree:
    compare root,left,right
 3. Invert Tree:
    use temp node and interchange the values of root.left and root.right

### HashMap:
O(1) lookup

### prefix sum:
running cumlative sum

# DFS
root -> left -> right

### BFS:
level order traversal using queue

### Balanced binary tree:
Height difference <=1

### Diameter of binary tree:
Left height + right Height

### time coplexities
linear search-O(n)
hashMap lookup-O(1)
binary search- O(log n)
linked list traversal-O(n)
tree DFS-O(n)
tree BFS-O(n)

The time complexity of both Depth-First Search (DFS) and Breadth-First Search (BFS) is O(n) for a tree because they both maintain a visited structure to ensure a spanning tree with no circuits. This means that for each node, either the node itself is visited, or its children are explored. Since each node is visited at least once, the total time complexity is O(n). Additionally, the time complexity is O(V+E) because each node is processed exactly once, and the sum of the sizes of the adjacency lists of all the nodes is E (total number of edges). Therefore, the total time complexity is O(n).

### Strongest pattern
prefix sum
valid parenthesis
two sum

### weakest pattern
prefix sum
trees
recursion

# common mistakes made

index error
map.put missing
wrong shrink
wrong mid
prefix confusion
boundary error
wrong shrink
using hashmap instead of hashset
wrong binary search boundary
queue front/reat confusion
linked lists(null issues,pointer updates)

---

## 2. Java Deep Concepts
JVM, memory, collections, multithreading insights.

---

## 3. Debugging Lessons
Real bugs and what they taught me.

---

## 4. Interview Mistakes
Mistakes during practice and corrections.

---

## 5. System Design Concepts
Scalability, APIs, databases, architecture.

---

## 6. AI Engineering Notes
Deployment, pipelines, practical ML systems.

AI systems are just the systems that take input and produce the output