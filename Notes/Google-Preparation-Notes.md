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


### Pattern: Sliding Window (Fixed Size)

Used when subarray of size k needed.

Steps:
1. Compute first window
2. Move window
3. Add next
4. Remove previous

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