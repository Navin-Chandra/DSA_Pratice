-- Write a solution to find the IDs of the invalid tweets. 
-- The tweet is invalid if the number of characters used 
-- in the content of the tweet is strictly greater than 15.

-- SELECT TWEET_ID FROM TWEETS WHERE LENGTH(CONTENT) > 15

select tweet_id from Tweets where char_length(content) > 15


-- Key Differences:
-- Function	Measures	Depends on Characters or Bytes
-- CHAR_LENGTH()	Number of characters in a string	Characters (e.g., "a" = 1, "💖" = 1)
-- LENGTH()	Number of bytes in a string	Bytes (depends on encoding; e.g., UTF-8: "a" = 1 byte, "💖" = 4 bytes)

-- When to use what?

--     Use CHAR_LENGTH() if you're checking for user-visible text length (most common case).

--     Use LENGTH() if you care about actual storage or byte size (e.g., file limits, encoding constraints).