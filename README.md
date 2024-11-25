<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Chakra+Petch&size=30&duration=1300&pause=500&color=888888&center=true&vCenter=true&width=630&lines=UBCO+Hackathon+Sustainability+Project"/>
  </a>
</p>

# Team Members
* ge0de
* JDMmahdi
* Ayyhab

# About The Project

## Inspiration
The huge frustration with wasting time in traffic and its negative repercussions on our environment motivated us to create an AI-based solution. Our primary goal was to use the technology of machine learning (ML) to reduce congestion and promote sustainability by optimizing resource utilization.

## What It Does
The project forecasts traffic volume based on inputs like the hour of the day, temperature, and whether it's a holiday. By studying these patterns, planners and users can prepare for traffic congestion and minimize its effects.

## Conclusion
Based on the correlation graphs shown graphs in the presentation, there was an evident correlation between the days being holidays and the hours of the days:
- Hours of the day: The traffic peaked at the hours 7 am and 16 pm, which has a correlation between people going and coming back from work.
- Temperature: No visible relation between temperature and traffic since 99.9% of the data was accumulated in the temperatures -25 to 30 Celsius.
- Holidays: Based on the graph, the traffic was lower on the holidays, generally.

## How We Built It
To process and analyze data from the Metro Interstate Traffic Volume dataset, we used Python along with libraries like Pandas, NumPy, Scikit-learn (for machine learning), Matplotlib, and Seaborn for data visualization. The core algorithm, Random Forest Regressor, was built into a Streamlit wrapper for user interaction.

## Challenges We Ran Into
The first challenge was understanding the dataset and preprocessing it for training our model. Another challenge was ensuring that correlational variables like holidays and traffic volume were captured accurately by the regression model.

## Accomplishments That We're Proud Of
In summary, we successfully built a working regression model that predicts traffic volume accurately and can be considered reliable. We also visualized the dataset insights and regression line, demonstrating the power of machine learning applied in real-world scenarios.

## What We Learned
We gained a deeper understanding of how machine learning detects patterns in data and differentiates them from background noise. Additionally, we learned how to create web applications using Streamlit to make our models accessible and user-friendly.

## What's Next For Sustainability Hackathon Project
There is room for improvement. We can refine the model with more data sources, such as live traffic updates. Additionally, we plan to scale the application to deliver real-time recommendations for rerouting traffic and optimizing resources, further maximizing sustainability.

## Additionally:
To predict traffic, we applied the Random Forest Regressor in our code. For visualizations, we used Matplotlib and Seaborn. We used Streamlit to create an easy and user-friendly interface for input and data visualization, as demonstrated in our project code.
