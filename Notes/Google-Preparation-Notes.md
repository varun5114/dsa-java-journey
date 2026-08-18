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

# for(int i = 0; i < n; i++) {
#    System.out.println(i);
# }     
The loop executes n times → O(n) time.

But we're not creating an array, HashMap, list, etc. that grows with n.

So:

Time  = O(n)
Space = O(1)

# for(int i = 0; i < n; i++) {
#  for(int j = 0; j < n; j++) {
#       System.out.println(i + j);
#   }
# }
Why O(n²)?

for(i = 0; i < n; i++) {       // n times
    for(j = 0; j < n; j++) {   // n times
    }
}

So:

n × n = n²

But again, we're not storing n² elements anywhere.

Therefore space is O(1).

# while(left <= right) {
#  int mid = (left + right) / 2;
#   ...
# }
Every iteration reduces the search space approximately by half:

n
↓
n/2
↓
n/4
↓
n/8
...

Therefore:

Time = O(log n)

But you're only storing:

left
right
mid

That's a fixed number of variables.

Therefore:

Space = O(1)

# for(int i = 0; i < n; i++) {
#  map.put(nums[i], i);
# }
Because we're looping through every element, we perform n insertions.

Therefore:

Time  = O(n)
Space = O(n)

Your space complexity is correct. ✅

Your explanation:

"the lookup is faster but the storage consumes space of n"

The storage part is right.

But this isn't really a lookup operation—we are building/populating the HashMap.

So the for loop itself makes the time O(n).

* Loops affect time; data structures/allocations affect space.

### int sum = 0;
# for(int i = 0; i < n; i++) {
#  sum += nums[i];
# }
Time  → O(n)
Space → O(1)

Your reasoning is correct.

Even though sum changes n times, it is still one variable, not n variables.

A useful distinction:

Changing a variable repeatedly does not increase space complexity.

# int[] copy = new int[n];
# for(int i = 0; i < n; i++) {
#  copy[i] = nums[i];
# }
Time  → O(n)
Space → O(n)

Because:

int[] copy = new int[n];

allocates an array capable of holding n elements.

# HashSet<Integer> set = new HashSet<>();

# for(int n : nums) {
#  set.add(n);
# }
Time  → O(n)
Space → O(n)

Your observation about the worst case is important.

For example:

nums = [1,2,3,4,5]

The HashSet stores 5 elements:

Space = O(n)

But:

nums = [1,1,1,1,1]

The HashSet stores only:

{1}

So actual space could be smaller.

But Big-O asks us to describe the worst-case growth, therefore:

O(n)

# for(int i = 0; i < n; i++) {
#  for(int j = 0; j < n; j++) {
#       System.out.println(i + j);
#   }
# }
Time  → O(n²)
Space → O(1)

Your reasoning is basically right.

One small improvement:

Don't say:

"because it executes 2 loops of n"

because that could make you think two loops always mean O(n²).

The important thing is that the loops are nested:

for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        ...
    }
}

The inner loop executes n times for every iteration of the outer loop:

n × n = n²

That's why it's O(n²).

If the loops were sequential:

for (...) { }   // n

for (...) { }   // n

then:

O(n) + O(n) = O(n)

not O(n²).

# for(int i = 0; i < n; i++) {
#  for(int j = i + 1; j < n; j++) {
#       System.out.println(i + j);
#   }
# }
You wrote:

O(n log n)

* The correct answer is:

* Time  → O(n²)
* Space → O(1)

The code was:

for(int i = 0; i < n; i++) {
    for(int j = i + 1; j < n; j++) {
        System.out.println(i + j);
    }
}

The important part is that the loops are nested.

The iterations are approximately:

(n-1) + (n-2) + (n-3) + ... + 1

which gives:

n(n-1)/2

Ignoring constants:

O(n²)
Why NOT O(n log n)?

O(n log n) usually comes from something like:

binary search performed n times
divide-and-conquer algorithms
merge sort

Simply having two nested loops does not always automatically mean O(n²), but here it does because the inner loop runs a linear number of times.

Your space answer is correct:

O(1)

because you're not creating an additional data structure that grows with n.

# for(int i = 0; i < n; i++) {
#  int j = i;
#   while(j < n) {
#       j++;
#   }
# }
You wrote:

O(n log n), O(1)
The inner loop does not halve anything.

For each i:

i = 0 → n iterations
i = 1 → n-1 iterations
i = 2 → n-2 iterations
...
i = n-1 → 1 iteration

Total:

n + (n-1) + (n-2) + ... + 1

This is:

n(n+1)/2

Therefore:

Time  → O(n²)
Space → O(1) ✅
Key lesson

A loop becoming shorter on every outer iteration doesn't mean O(n log n).

You need to ask:

Is the problem size being divided by a constant factor?

Here, no. We're subtracting roughly one each time.

# int i = 0;
# while(i < n) {
#  i = i * 2 + 1;
# }
You wrote:

O(n log n), O(n log n)

❌ Both are wrong.

Code:

int i = 0;


while(i < n) {
    i = i * 2 + 1;
}

Look at what happens:

i = 0
i = 1
i = 3
i = 7
i = 15
i = 31
...

The value of i approximately doubles every iteration.

Therefore the number of iterations is:

log₂(n)

So:

Time → O(log n)

And what are we storing?

Only:

i

One variable.

Therefore:

Space → O(1)
Correct answer:
Time  → O(log n)
Space → O(1)

Your mistake here is particularly important:

O(log n) time does NOT automatically mean O(log n) space.

Space depends on what you're storing, not how many iterations happen.

# for(int i = 0; i < n; i++) {
#  for(int j = 0; j < 10; j++) {
#       System.out.println(i + j);
#   }
# }
You wrote:

O(n*1), O(1)

✅ Correct.

Simplify:

O(n × 1)
= O(n)

The inner loop runs exactly 10 times, regardless of how large n becomes.

Therefore:

Time  → O(n)
Space → O(1)

This is a good example of why:

Two nested loops ≠ automatically O(n²).

The inner loop has a constant bound.

# for(int i = 1; i < n; i *= 2) {
#  System.out.println(i);
# }

You gave:

O(n*(n+1)/2), O(1)

✅ Your reasoning is correct, but in an interview/LeetCode answer, simplify it to:

Time  → O(n²)
Space → O(1)

Because:

2
n(n+1)
	​

=
2
n
2
+n
	​


We ignore constants and lower-order terms:

O(n²)

So your mathematical understanding is good.

# for(int i = 0; i < n; i++) {
#  for(int j = 0; j < i; j++) {
#       System.out.println(i + j);
#   }
# }

You said:

"I don't know time but space = O(1)"

❌ Time needs correction.

The code was:

for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
        System.out.println(i + j);
    }
}

The inner loop executes:

0 + 1 + 2 + 3 + ... + (n-1)

That's:

2
n(n−1)
	​


Therefore:

Time  → O(n²)
Space → O(1)

So C is the one you need to add to your revision list.
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