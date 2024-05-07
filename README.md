# News classification API with Docker

Image available on [Docker hub](https://hub.docker.com/r/timee98642/classify-news-app)

## Repo structure
```
├── app/
│   ├── model/
│   │   ├── classify_news_pipeline-0.1.0.pkl
│   │   ├── df_file.csv
│   │   ├── model-dev.ipynb
│   │   └── model.py
│   └── main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
└── requirements.txt
```

## Building the API locally

Step 0: `git clone https://github.com/divakaivan/classify-news-app.git` in your terminal

### Step 1: Build the Docker image

Make sure you are in the base directory and run `docker build -t classify-news-app .` .

### Step 2: Run the Docker container

`docker run -p 80:80 classify-news-app`.

### Step 3: Visit 0.0.0.0 🥳
You should see something like:
```js
{
  "health_check": "OK",
  "model_version": "0.1.0"
}
```

It is built using FastAPI, so if you go to `/docs` you can find more info about the endpoints. 

## What it can do

Given a piece of news as *string*, it will return Politics, Sport, Technology, Entertainment, Business and each class' probability in a *dictionary*

### Use case

Go to `/docs`

![image](https://github.com/divakaivan/classify-news-app/assets/54508530/3c982fa5-892d-4ccf-b40e-0d8a618579e2)

Click on POST a dropdown will open, and on the right side click on `Try it out`

![image](https://github.com/divakaivan/classify-news-app/assets/54508530/f7a5f89b-501b-478c-aa74-8eba1ab9f9dd)

Click on `Execute`, and below is the response

![image](https://github.com/divakaivan/classify-news-app/assets/54508530/1498311c-2460-483e-97d5-252e9cddbf7a)

Props to AssemblyAI for the [tutorial](https://youtu.be/h5wLuVDr0oc)
