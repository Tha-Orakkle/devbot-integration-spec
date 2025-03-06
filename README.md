# DEVBOT INTEGRATION SPECIFICATION

## Description

The integration specification for devbot for [telex](https://telex.im). Telex is an event monitoring application where you can get notifications on different events occuring on your server etc. This is done with the help of integrations created to fit whatever purpose you need the application for.

The devbot integration creates an interface for DevOp engineers to get log events from their GitHub Action workflows. It also serves as an assistant that provides relevant AI generated responses to DevOps and CI/CD-related questions.

This specification contains the necessary information to plug the integration to your Telex channel.

### Specification format

```json
{
    "data": {
        "date": {
            "created_at": "2025-02-17",
            "updated_at": "2025-02-17",
        },
        "descriptions": {
            "app_description": "An AI-powered assistant that provides responses to Devops and CI/CD related queries in form of github actions workflows run logs or as ai-generated response",
            "app_name": "ai-chatbot-for-devops",
            ...
        },
        "integration_category": "DevOps & CI/CD ",
        "integration_type": "modifier",
        ...
    }
}
```

- spec available at [devbot-integration-specification](https://devbot-integration-spec.up.railway.app/api/integration.json)

## Author

tha_orakkle (adegbiranayinoluwa.paul@yahoo.com)
