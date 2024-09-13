from config import TOKEN
import pandas as pd

model = tf.keras.models.load_model('')
predictions = model.predict(data)  