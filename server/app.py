import firebase_admin
from firebase_admin import firestore

databaseURL = "https://test-firebase-python-768e3.asia-southeast1.firebasedatabase.app"
# ? Get cred from firebase's service account
cred = firebase_admin.credentials.Certificate("./cred.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# * Write a new document
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

# * Read document
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')