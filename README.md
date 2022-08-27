![Screenshot](images/aws_sam.png)

# Data Ingest Project with AWS Lambda

### What is Serverless?
Serverless are systems where developers can deploy any system by developing on the cloud without using hardware and network infrastructure.
AWS lambda will be used in this project. Work will be done on how to deploy a local code to AWS lambda. Project purpose: We will make an example of how to import data to Amazon RDS with AWS Lambda by pulling data from API. We will learn how to use AWS SAM, which is one of the most important steps.

This project will contain source code to support SAM CLI.

- dataIngest - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- template.yaml - A template that defines the application's AWS resources.

### Deploy the application

To use the SAM CLI, you need the following tools.
The purpose of downloading Docker is to run the code locally.
You can download one of these versions as it supports versions 3.6 to 3.9 while running on AWS lambda.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)


### Enviroment variables
After downloading the applications, we can check the environment variables settings and make them work from all paths.


## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
dataIngest$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
dataIngest$ sam local invoke HelloWorldFunction --event events/event.json
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name dataIngest
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
