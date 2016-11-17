routes_in = (
  ('/admin','/admin'),
  ('/realtime$anything','/realtime$anything'),
  ('/admin/$anything','/admin/$anything'),
  ('/$app/appadmin','/$app/appadmin'),
  ('/$app/static/$anything','/$app/static/$anything'),
  ('/robots.txt','/SOL/static/robots.txt'),
  ('/static/$anything','/SOL/static/$anything'),
  ('/query/results$anything','/SOL/invoicetest/search$anything'),
  ('/departures/$anything','/SOL/test/departures/$anything'),
  ('/', '/SOL/default/home'),
  ('/sales','/SOL/sales/show_table/0/0'),
  ('/ziro-music-festival/','/SOL/default/particular_event/ziro-festival-of-music-2015'),
  ('/unsubscribe','/SOL/invoicetest/unsubscribe'),
  ('/dashboard','/SOL/default/dashboard'),
  ('/reviews','/SOL/loader2/sol_review'),
  ('/weekend-getaways/from-$anything', '/SOL/test/weekend_getaways/from-$anything'),
  ('/corporate-tours/','/SOL/function_new/corporate'),
  ('/corporate-tour/$anything','/SOL/function_new/corporatePdf/$anything'),
  ('/trip/$anything', '/SOL/default/trip/$anything'),
  ('/all-events$anything','/SOL/default/event$anything'),
  ('/particular-event/$anything','/SOL/default/particular_event/$anything'),
  ('/fixed-departure/$anything','/SOL/default/fixed_departure/$anything'),
  ('/campaign/$anything','/SOL/default/ad/$anything'),
  ('/location/$anything','/SOL/default/location/$anything'),
  ('/blogs$anything','/SOL/blog/blogList$anything'),
  ('/search/$anything','/SOL/loader/betterSearch/$anything'),
  ('/equipment-rental','/SOL/function_new/equipment_rental'),
  ('/product-detail/$anything','/SOL/function_new/desc_product/$anything'),
  ('/rental-cart','/SOL/function_new/cart'),
  ('/order-rental','/SOL/function_new/order_rental'),
  ('/user$anything','/SOL/default/user$anything'),
  ('/about-us/','/SOL/default/aboutus'),
  ('/thank-you','/SOL/default/thankyou'),
  ('/sitemap.xml','/SOL/BlackBox/sitemap.xml'),
  ('/tag$anything','/SOL/default/tag$anything'),
  ('/profile$anything','/SOL/BlackBox/user$anything'),
  ('/SOL/default/$anything','/SOL/default/$anything'),
  ('/SOL/loader/$anything', '/SOL/loader/$anything'),
  ('/SOL/BlackBox/$anything','/SOL/BlackBox/$anything'),
  ('/(?P<any>[a-zA-Z0-9_-]+)/', '/SOL/blog/blogs/\g<any>'),
)
routes_out = [(x,y) for (y,x) in routes_in[:-1]]
routes_out.append(('/SOL/blog/blogs/(?P<any>[a-zA-Z0-9_-].*)','/\g<any>/'))

routes_onerror = [
  ('SOL/*','/SOL/default/handle_error')
]

