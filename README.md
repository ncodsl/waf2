# Vercel-Boiler
A "boiler" template for Flask applications hosted with Vercel. The aim of this template is to serve as a foundational frame for further development.

## Instructions
To host a Flask app on Vercel, you will first need to create a new project on Vercel and connect it to your GitHub or GitLab repository. Then, you will need to create a vercel.json file in the root of your project with the following contents:

### vercel.json
```
{
  "version": 2,
  "builds": [
    {
      "src": "sample.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/.*",
      "dest": "sample.py"
    }
  ]
}
```

This file tells Vercel how to build and deploy your Flask app. The src property in the builds array specifies the entry point of your app (in this case, app.py), and the use property specifies the Vercel builder that should be used to build and deploy the app (in this case, the Python builder).

*NOTE: Be sure to edit builds["src"] and routes["dest"] for Vercel to read the application correctly.*


Next, you will need to create a requirements.txt file in the root of your project, which should contain a list of all the Python packages that your app depends on. Best way to do so is to run the following code on the command-line interface (CLI):

```
pip freeze > requirements.txt 
```
This file will be used to install the required dependencies when your app is deployed to Vercel.

Finally, you can deploy your app to Vercel by running the following command from the root of your project:

```
vercel
```

This will start the deployment process, and your app will be live at a URL provided by Vercel once the deployment is complete.

Note: You will need to have the Vercel CLI installed on your computer to run the vercel command. To install the CLI, run npm install -g vercel (assuming you have npm installed on your computer).

Alternatively, one can use [Vercel's dashboard](https://vercel.com/) to create a Vercel project with a more intuitive interface.

![Flask and Vercel](https://i.imgur.com/RUKfGrA.png)


