# Challenge #9

**Visual to Natural Language Converter**

2025 PDA Vision Theme: 
Knowledge

**Summary**

With the explosion of natural language technology companies are suddenly able to ingest huge amounts of documentation data to query easily and simply. For the first time ever, unstructured data can be easily and quickly analysed to pull insight like never before.

With these new opportunities, new challenges have arisen. One major challenge is even if you can ingest huge amounts of documentation, it is difficult to pull insight from visuals that don’t have a clear way to convert to text. 

For this challenge, we want teams to create a system that converts images of tables and graphs into text that can be read by large language models. With this, we can query huge quantities of academic papers and reports without access to the original data, while still gaining insight into the data based visuals within.

**Pain Points**

- I want to be able to use images of graphs and tables as datasets for natural language models
- I want to be able to convert images into text for natural language models to understand
- I want to be able to pull relevant data from images of visualisations and query them with natural language

**Personas**

- As a project profession, I want to be able to query project documentation using natural language processing, So that I can quickly gain insight and information from the huge quantities of documentation available

- As a data analyst, I want to quickly ingest data from unstructured documentation, So I can use that data to gain project insight

- As a document controller, I want the large quantities of documents I control to bring as much value to future projects as possible using natural language, So that insight can be gained quickly and I don’t have to expend significant resources into pulling data from documentation

**Context**

Recent explosive growth in large language models and natural language models has seen a drastic change in how we work and the future of data analysis. A recent plugin for OpenAI’s GPT natural language model is ChatPDF, a tool to convert a pdf into natural language, pass it into the large language model and allow users to ask question on the contents of the PDF. 

This new functionality opens up an incredible amount of possibilities. What if we can pass large quantities of unstructured documentation into it and tap into what was previously inaccessible data? Can we finally make use of all the data we have that would be too cumbersome to convert into structured data?

This technology is already opening door we never thought imaginable but one major problem is that we cannot pass images and visualisations into a natural language model. Although we can query and structure the text, the data locked within visualisations is still beyond our reach.

Of course, in an ideal world all the data we used to create the visualisation in our documents is still accessible directly. Unfortunately, data can become lost for any number of reasons and finding the source of each visualisation would take us back to the same issue we had before, a quantity of work we don’t have the resourcing to do.

For this challenge, teams will need to create a system of converting images of data visuals into the raw data itself. You will need to consider what visuals can be more easily converted and where we are going to struggle the most. Teams will also need to consider the risk of automation, if we are converting large amounts of images to natural language. You should assume that results will not be manually reviewed and try to create a system that will not muddy the data with false results.

**Dataset Description**

You will be provided with a collection of images taken directly from publicly available documentation and reports from GLEEDS. These images are graphs and visualisations of all kinds that contain data that is not readily available. 


**Output**

Teams will need to create a method for quickly converting images of data visualisation into machine readable text. Consider what options you have to ingest as much as possible and how you can reject images that wont produce an accurate result.

Teams should consider what options they have to identify information only available within the visual itself. For example, how can we record the height of a bar chart when the number associated with it is only available on the axis.


**Benefits**

By clearing this technical hurdle we potentially open the door to finding value within countless documents and historical records. It offers an option of reclaiming lost data and transforming abandoned documents into relevant data that can allow us to gain much deeper insight into our projects.

**Useful Resources**

https://www.chatpdf.com/