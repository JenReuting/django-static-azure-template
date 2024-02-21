# Abstract Models and Mixins

We have abstract models (~/core/models.py) that our other models inherit from. This allows us to add common fields and methods to our models without having to repeat ourselves.

The `UUIDBaseModel` replaces the incrementing primary key with a more secure UUID. The `AutoIncrementBaseModel` is a base model that uses the default Django primary key, while still also providing the common fields defined in the `CommonFieldsMixin`.