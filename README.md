# MemFlix — Deployment Package

## Files
| File         | URL after deploy          | Purpose                          |
|--------------|---------------------------|----------------------------------|
| index.html   | yourdomain.vercel.app/    | Main app (she sees this)         |
| admin.html   | yourdomain.vercel.app/admin | Your private upload panel      |
| firebase-config.js | included by both pages | Firebase project config |
| data/memflix-data.json | yourdomain.vercel.app/data/memflix-data.json | Local seed data |
| vercel.json  | (config — don't delete)   | Routing rules for Vercel         |

## Recommended Storage Setup
For more than a few photos, use Firebase:

1. Create a Firebase project.
2. Enable Firestore Database.
3. Enable Cloud Storage for Firebase. Pick an eligible region if you want the free 5 GB-month storage quota.
4. In Project settings → General → Web app, copy the Firebase config into `firebase-config.js`.
5. Deploy this folder to Vercel.

Example `firebase-config.js`:

```js
window.MEMFLIX_FIREBASE_CONFIG = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT",
  storageBucket: "YOUR_PROJECT.firebasestorage.app",
  appId: "YOUR_APP_ID"
};
```

## Firebase Rules
For a private personal app, start locked down and temporarily open writes only while uploading from `/admin`.

Firestore rules for simple testing:

```txt
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```

Storage rules for simple testing:

```txt
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if true;
    }
  }
}
```

These rules are convenient for setup, but they are public. For a real private deployment, add Firebase Auth and restrict writes to your admin account.

## Deploy Steps
Short version: upload this folder to GitHub, import the repo in Vercel, and deploy.

## URLs
- Main app:   https://your-project.vercel.app
- Admin:      https://your-project.vercel.app/admin

## Notes
- If `firebase-config.js` is filled in, MemFlix uses Firebase Firestore + Storage.
- If `firebase-config.js` is empty, the app falls back to local browser data and `data/memflix-data.json`.
- Use Admin → Export Data to download an updated `memflix-data.json` after editing.
- Browser-based static apps cannot write changes back into GitHub/Vercel files automatically without a cloud backend.
