import json

from commons import get_model, get_tensor

with open('class_to_idx.json') as f:
	class_to_idx = json.load(f)


idx_to_class = {v:k for k, v in class_to_idx.items()}

model = get_model()

def get_blood_type(image_bytes):
	tensor = get_tensor(image_bytes)
	outputs = model.forward(tensor)
	_, prediction = outputs.max(1)
	category = prediction.item()
	class_idx = idx_to_class[category]
	blood_type =[class_idx]
	return category, blood_type