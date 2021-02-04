from zenml.core.steps.preprocesser.base_preprocesser import BasePreprocesserStep

class MyCustomPreprocesser(BasePreprocesserStep):

    def preprocessing_fn(self, inputs: dict):
        outputs = inputs
        print(inputs)
        # your preprocessing logic goes here
        
        return outputs