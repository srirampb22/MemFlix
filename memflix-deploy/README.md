# 🎬 MemFlix — Deployment Package

## Files
| File         | URL after deploy          | Purpose                          |
|--------------|---------------------------|----------------------------------|
| index.html   | yourdomain.vercel.app/    | Main app (she sees this)         |
| admin.html   | yourdomain.vercel.app/admin | Your private upload panel      |
| vercel.json  | (config — don't delete)   | Routing rules for Vercel         |

## Deploy Steps
See the step-by-step guide Claude gave you.
Short version: zip this folder → vercel.com/new → drag & drop → done.

## URLs
- Main app:   https://your-project.vercel.app
- Admin:      https://your-project.vercel.app/admin

## Notes
- Credentials (Supabase/Cloudinary) are stored in YOUR browser only
- She needs to enter Supabase URL + key once when she first opens the app
- To avoid that, see "Hardcode credentials" section in the guide
