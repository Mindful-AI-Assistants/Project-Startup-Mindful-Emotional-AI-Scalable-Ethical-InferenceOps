
import random, os
import matplotlib.pyplot as plt

class FraudDetection:
    def __init__(self, threshold=0.8):
        self.threshold = threshold
        self.logs = []

    def predict(self, transaction):
        risk = transaction['amount']/5000 + random.uniform(0,0.5)
        decision = 'REJECT' if risk > self.threshold else 'APPROVE'
        self.logs.append({'id':transaction['id'], 'amount':transaction['amount'], 'risk':risk, 'decision':decision})
        return decision

    def audit(self):
        return self.logs

# simulate
transactions = [{'id':i, 'amount': random.randint(10,5000)} for i in range(1,51)]
model = FraudDetection(threshold=0.8)
for t in transactions:
    model.predict(t)

logs = model.audit()
approved = sum(1 for l in logs if l['decision']=='APPROVE')
rejected = len(logs) - approved
print(f"Total: {len(logs)} | Approved: {approved} | Rejected: {rejected}")

# scatter plot
os.makedirs('assets/diagrams', exist_ok=True)
amounts = [l['amount'] for l in logs]
decisions = [1 if l['decision']=='REJECT' else 0 for l in logs]
colors = ['#2ee6d6' if d==0 else '#ff4d6d' for d in decisions]

plt.figure(figsize=(8,4))
fig = plt.gcf(); fig.patch.set_facecolor('#0b1a1f')
ax = plt.gca(); ax.set_facecolor('#081018')
plt.scatter(amounts, decisions, c=colors, alpha=0.7)
ax.set_yticks([0,1]); ax.set_yticklabels(['APPROVE','REJECT'], color='white')
ax.set_xlabel('Transaction Amount (USD)', color='white')
ax.set_title('Fraud Detection Simulation', color='white')
ax.tick_params(colors='white')
ax.grid(True, linestyle='--', color='#073239', alpha=0.5)
plt.tight_layout()
plt.savefig('assets/diagrams/fraud_detection_simulation_dark.png', dpi=180, facecolor=fig.get_facecolor())
plt.close()
