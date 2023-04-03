# Automatic question's segmentation 


Here we develope a method to automaticaly associate tags to a stack overflow's post. We will use different machine learning nlp methods : First unsupervised with a bag of word and then supervided with word embeding. 

Data can be found at https://data.stackexchange.com/stackoverflow/query/new and extracted with the following querry :

DECLARE @start_date DATE
DECLARE @end_date DATE
SET @start_date = '2011-01-01'
SET @end_date = '2023-01-01'

SELECT p.Id, p.CreationDate, p.Title, p.Body, p.Tags,
p.ViewCount, p.CommentCount, p.AnswerCount, p.Score 
FROM Posts as p
LEFT JOIN PostTypes as t ON p.PostTypeId = t.id
WHERE p.CreationDate between @start_date and @end_date
AND t.Name = 'Question'
AND p.ViewCount > 20
AND p.CommentCount > 5
AND p.AnswerCount > 1
AND p.Score > 5
AND len(p.Tags) > 0


## Notebook 1 : Data preparation and analysis

In this first notebook the extracted data is processed and analysed.


## Notebook 2 : Test of supervised and unsupervised nlp alogithms
