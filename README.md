<h1 align="center">Flipkart Grid5.0</h1>
<h1 align="center">Team Name: Achintya</h1>
<h2>Team Members:</h2>
Vaibhav Ahuja<br>
Shounmay Darsh
<h2>Problem Statement:</h2>
<h3>Personalized Product Recommendations</h3>
The aim is to enhance user experience by implementing a personalized product ranking system.
Your task is to develop an algorithm or model that can generate accurate and relevant product
rankings for individual users. The ranking system should consider factors such as user
preferences, past interactions, product popularity, and user similarity. It should be able to predict
the most suitable products for a user based on their unique characteristics and preferences.
You are not provided with a specific dataset for this challenge. Instead, you are expected to
design and implement a solution that simulates user interactions and generates personalized
rankings. You can define user profiles, product categories, and interaction patterns within your
solution.
To evaluate the effectiveness of your solution, you should define appropriate metrics for
measuring the accuracy and relevance of the rankings. You should also provide a report
explaining your approach, describing the algorithms or techniques used, and discussing the
strengths and limitations of your solution
<h2>Solution:</h2>
<h3>1. Data Exploration (EDA):</h3>
The dataset encompasses multiple facets of an e-commerce platform such as events (e.g., view, add to cart, purchase), item details, and category structures. Our exploratory analysis revealed:<br>
•<b>Events Distribution: </b>Visual representation of various user actions.<br>
•<b>Temporal Trends:</b> The flow and frequency of user events over time.<br>
•<b>Item Popularity:</b> Identifying the top viewed and sold items.<br>
•<b>Category Insights:</b> Recognizing the most viewed and transacted categories.<br>
<h3>2. Feature Engineering:</h3>
To enrich our predictive model, we transformed the raw data into more insightful features:<br>

•<b>User-based Features:</b> Captured user behavior metrics like average time spent on the platform and the average number of items viewed.<br>
•<b>Item-based Features:</b> Metrics indicating item popularity based on different user events.<br>
•<b>User-item Interaction Features:</b> Details on the frequency and duration between user-item interactions.<br>
<h3>3. Model Building & Evaluation:</h3>
Our modeling approach used the Singular Value Decomposition (SVD) technique.<br>
•<b>Choice of SVD:</b> SVD's ability to discern latent factors in user-item matrices made it an apt choice. Its performance in recommendation scenarios further justified our pick.<br>
•<b>Hyperparameter Precision:</b> The GridSearchCV ensured our SVD model was precisely tuned. Parameters like n_factors, n_epochs, lr_all, and reg_all were meticulously selected to get the best out of our model.<br>
•<b>Training Strategy:</b> With the best parameters identified, the model was trained to recognize patterns, behaviors, and nuances in user-item interactions.<br>
•<b>Evaluation Rigor:</b> The model was then evaluated using the Mean Absolute Error (MAE) metric. To get a more holistic view, we also formulated an Accuracy Score and a Normalized Prediction Score.<br>
<h2> Quick Walkthorugh</h2>

![5fd04a8a-6cbc-4507-b877-92a4434ac78e](https://github.com/Shounmay/MartDashX_Grid5.0/assets/85643531/a51eff8e-7f6d-4c4b-a83a-07cfc38406a3)


To provide a user-friendly interface and a consolidated view of the prediction outcomes and e-commerce metrics, we've developed a state-of-the-art admin panel with the following features:<br>
•<b>Dashboard:</b> A centralized hub to get a snapshot of the overall e-commerce health.<br>
•<b>User Recommendations:</b> The heart of our solution, this page showcases the product recommendations for users, as derived from our SVD model. Here, you'll find pairs of user IDs alongside their recommended item IDs.<br>
•<b>Client Facing Products & Customers:</b> Overview of products available and details on the customer base.<br>
•<b>Transactions Overview:</b> A look into transactional patterns, offering insights into shopping behaviors.<br>
•<b>Sales Analytics:</b> Breakdown of sales, presented in daily and monthly overviews, to gauge business momentum.<br>
<h3>Limitations & Data Context:</h3>
It's important to note that while our user recommendations page is powered by genuine insights derived from our model, data on other admin panel pages is simulated. This decision stems from our limited access to expansive e-commerce datasets. The dummy data is meticulously crafted to provide a realistic view, but it's crucial for users to know its simulated nature.

This is not a limitation of the model's capability, but rather a constraint based on the available data. When equipped with a richer dataset, our model and platform are structured to be fully functional, scaling seamlessly to the data's granularity.
<h2>Deployed Link</h2>
https://martdashxtest.onrender.com/
<h2>Proof of Project (Detailed Model Explanation) </h2>
https://docs.google.com/document/d/1jIweoUURQ54izAWvCQMFH9Z538e_QomdO-qfI6-giEw/edit?usp=sharing
