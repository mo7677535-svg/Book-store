# Pustak Hub - Full-Stack Bookstore Application

> A modern, production-ready e-commerce bookstore built with Next.js, React, Supabase, and Tailwind CSS.

## 🎯 Quick Links

| Document | Purpose |
|----------|---------|
| **[BUILD_SUMMARY.md](./BUILD_SUMMARY.md)** | 📋 Overview of what was built |
| **[QUICK_START.md](./QUICK_START.md)** | ⚡ Get up and running in 5 minutes |
| **[COMPLETE_SETUP.md](./COMPLETE_SETUP.md)** | 📚 Full technical documentation |
| **[APP_FEATURES.md](./APP_FEATURES.md)** | ✨ Complete feature list |

---

## 🚀 Get Started

### 1. Set Environment Variables

Create `.env.local`:
```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

---

## ✨ Features

- **Product Catalog** - Browse 12 pre-loaded books
- **Shopping Cart** - Add/remove items, manage quantities
- **User Auth** - Email/password signup and login
- **Secure Checkout** - Create orders with RLS protection
- **Order History** - View past orders and details
- **Responsive Design** - Works perfectly on all devices
- **Database Persistence** - All data stored in Supabase PostgreSQL
- **Security** - Row Level Security, auth checks, data isolation

---

## 📱 Pages

| Page | URL | Purpose |
|------|-----|---------|
| Home | `/` | Featured products & catalog |
| Products | `/products` | All books |
| Details | `/product/[id]` | Book details |
| Cart | `/cart` | Shopping cart |
| Login | `/auth/login` | User login |
| Sign Up | `/auth/sign-up` | Create account |
| Profile | `/profile` | User dashboard |
| Order | `/order/[id]` | Order details |

---

## 🏗️ Architecture

```
Next.js 16 App
    ├── React Components
    ├── Tailwind CSS Styling
    └── Next.js API Routes
            ↓
    Supabase Backend
        ├── PostgreSQL Database
        ├── Row Level Security
        └── Authentication
```

---

## 📊 Database

**4 Tables** with RLS policies:

- **products** - 12 books (public read)
- **orders** - User orders (user RLS)
- **order_items** - Order details (user RLS)
- **profiles** - User data (user RLS)

---

## 🔐 Security

- ✅ Supabase Row Level Security
- ✅ User authentication required
- ✅ Password hashing
- ✅ Secure session management
- ✅ Protected API routes
- ✅ User data isolation

---

## 📦 Tech Stack

- **Next.js 16** - React framework
- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS 4** - Styling
- **Supabase** - Auth + Database
- **Lucide React** - Icons

---

## 🧪 Testing

Try these features:

1. Browse products on home page
2. View product details
3. Add items to cart
4. Create new account
5. Login and checkout
6. View order history
7. Mobile responsive design

---

## 🚢 Deployment

### Deploy to Vercel (1-click)

1. Push code to GitHub
2. Import in Vercel
3. Add environment variables
4. Deploy!

### Other Platforms

Works on any Node.js host:
- Railway
- Netlify
- AWS
- DigitalOcean

---

## 📖 Documentation

### For Setup
→ See [QUICK_START.md](./QUICK_START.md)

### For Full Details
→ See [COMPLETE_SETUP.md](./COMPLETE_SETUP.md)

### For Features
→ See [APP_FEATURES.md](./APP_FEATURES.md)

### For Overview
→ See [BUILD_SUMMARY.md](./BUILD_SUMMARY.md)

---

## 🎯 Project Structure

```
app/
├── page.tsx                    # Home
├── products/page.tsx          # All products
├── product/[id]/page.tsx      # Product detail
├── cart/page.tsx              # Cart
├── auth/login/page.tsx        # Login
├── auth/sign-up/page.tsx      # Sign up
├── profile/page.tsx           # Profile
├── order/[id]/page.tsx        # Order detail
└── api/
    ├── products/[id]/route.ts # Product API
    └── orders/create/route.ts # Order API

components/
├── header.tsx                 # Navigation
├── footer.tsx                 # Footer
├── add-to-cart-button.tsx    # Cart button
└── logout-button.tsx          # Logout button

lib/
├── supabase/
│   ├── client.ts             # Browser client
│   ├── server.ts             # Server client
│   └── proxy.ts              # Middleware
└── cart.ts                    # Utilities

styles/
└── catalog.css               # Styling

scripts/
├── 001_create_tables.sql    # DB schema
└── 002_seed_products.sql    # Product data
```

---

## 🔧 Configuration

### Environment Variables

```env
NEXT_PUBLIC_SUPABASE_URL       # Your Supabase URL
NEXT_PUBLIC_SUPABASE_ANON_KEY # Your Supabase key
```

### Build

```bash
npm run build   # Production build
npm run start   # Start server
npm run dev     # Development
```

---

## 🐛 Troubleshooting

### Products not loading?
- Check Supabase URL is correct
- Verify RLS allows public read

### Cart items disappear?
- Ensure localStorage is enabled
- Check browser settings

### Checkout fails?
- Ensure user is logged in
- Check API logs

### Images not showing?
- Using placeholder URLs
- Add real URLs in database

---

## 🎓 Learning Value

This project teaches:

- Full-stack development
- Next.js patterns
- React best practices
- Database design
- Security implementation
- API design
- TypeScript
- Responsive design

---

## 📈 Performance

- Server-side rendering where possible
- Database query optimization
- CSS/JS bundling
- Browser caching
- Vercel edge network

---

## 💡 Customization Ideas

- Add product search
- Implement reviews/ratings
- Add wishlist feature
- Email order confirmation
- Admin dashboard
- Payment processing (Stripe)
- Advanced filtering
- User recommendations

---

## 📞 Getting Help

1. **Setup Issues** → [QUICK_START.md](./QUICK_START.md)
2. **Technical Questions** → [COMPLETE_SETUP.md](./COMPLETE_SETUP.md)
3. **Feature Questions** → [APP_FEATURES.md](./APP_FEATURES.md)
4. **Overview** → [BUILD_SUMMARY.md](./BUILD_SUMMARY.md)

---

## 📄 License

Open source project. Feel free to use and modify.

---

## ✅ Status

**Status**: Ready for production use and deployment

- ✅ All features implemented
- ✅ Security configured
- ✅ Database schema complete
- ✅ 12 books pre-loaded
- ✅ Fully documented
- ✅ Production ready

---

## 🎉 Ready to Launch?

1. Configure `.env.local` with Supabase credentials
2. Run `npm install` and `npm run dev`
3. Test the application locally
4. Push to GitHub
5. Deploy to Vercel
6. Customize and enjoy!

---

**Built with ❤️ using Next.js 16 + Supabase**

Last Updated: March 2024
