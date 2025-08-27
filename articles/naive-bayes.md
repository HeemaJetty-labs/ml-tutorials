## Naive Bayes Algorithm explained with few commonly used examples. I have mentioned the formula below. For beginners, try to understand the use cases and then relate the formula derivation and logic.

## What is Naive Bayes?

Naive Bayes is a simple and fast **classification algorithm** based on the principles of probability and Bayes’ theorem. It’s called “naive” because it assumes all features (inputs) are independent of each other.

## Where is it Used?

- **Spam detection** (deciding if an email is spam or not)
- **Sentiment analysis** (finding if a review/comment is positive or negative)
- **Document and news categorization**

## The Basic Idea

Naive Bayes tries to find the **probability that a data point belongs to a certain class** (“spam” or “not spam”, “yes” or “no”, etc.) **based on its features** (like the words in an email).

## How Does it Work?

- It uses **Bayes’ theorem**:

  $$
  P(\text{Class} | \text{Features}) = \frac{P(\text{Class}) \cdot P(\text{Features}|\text{Class})}{P(\text{Features})}
  $$

  - $$P(\text{Class}|\text{Features})$$: Probability that the item is in this class, given its features (**posterior**)
  - $$P(\text{Class})$$: General probability of this class (**prior**)
  - $$P(\text{Features}|\text{Class})$$: Probability of observing these features if the item is in the class (**likelihood**)
  - $$P(\text{Features})$$: General probability of these features (**evidence**)

- The “naive” part: It multiplies the probabilities of each feature independently:

  $$
  P(\text{Features}|\text{Class}) = P(x_1|\text{Class}) \cdot P(x_2|\text{Class}) \cdot ... \cdot P(x_n|\text{Class})
  $$

## Simple Example

Let’s say you want to predict if an email is **spam** based on two features: if it has the word "offer" and if it has an attachment.

Naive Bayes calculates:

1. Probability of spam emails in the dataset ($$P(\text{Spam})$$)
2. Probability an email contains "offer" given it’s spam ($$P(\text{"offer"}|\text{Spam})$$)
3. Probability an email has an attachment given it’s spam ($$P(\text{Attachment}|\text{Spam})$$)
4. Multiplies these and compares the same calculation for "not spam"

## Why Use Naive Bayes?

- **Very fast** and highly scalable, even with lots of data
- Works surprisingly well even if the “independence” assumption is not 100% true
- Great “first model” to try for many text and tabular classification tasks

***

**Summary:**  
Naive Bayes is a simple yet powerful probabilistic model that can help classify data by assuming features are independent and by leveraging the basic rules of probability.

## Code Examples
supervised-learning/classification/naivebayes/naivebayes-basic.py
