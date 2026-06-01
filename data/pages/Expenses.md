- Expenses
- Всего на странице
	- #+BEGIN_QUERY
	  {
	    :title [:p "AUD"]
	    :query [
	      :find (sum ?n)
	      :in $ ?current-page
	      :with ?b
	      :where
	        [?p :block/name ?current-page]
	        [?b :block/page ?p]
	        [?b :block/properties ?prop]
	        [(get ?prop :aud) ?v]
	        [(* 1 ?v) ?n]
	    ]
	    :inputs [:current-page]
	    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
	  }
	  #+END_QUERY
- ## 2026
	- Год 2026
	  collapsed:: true
		- #+BEGIN_QUERY
		  {
		    :title [:p "AUD 2026"]
		    :query [
		      :find (sum ?n)
		      :with ?b
		      :where
		        [?b :block/properties ?prop]
		        [(get ?prop :aud) ?v]
		        [(* 1 ?v) ?n]
		        [?b :block/parent ?parent]
		        [?parent :block/refs ?ref]
		        [?ref :block/name ?name]
		        [(clojure.string/starts-with? ?name "2026-")]
		    ]
		    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
		  }
		  #+END_QUERY
	- По месяцам
	  collapsed:: true
		- collapsed:: true
		  #+BEGIN_QUERY
		  {
		    :title [:p "AUD по месяцам 2026"]
		    :query [
		      :find ?month (sum ?n)
		      :keys month aud
		      :where
		        [?b :block/properties ?prop]
		        [(get ?prop :aud) ?v]
		        [(* 1 ?v) ?n]
		        [?b :block/parent ?parent]
		        [?parent :block/refs ?ref]
		        [?ref :block/name ?date]
		        [(clojure.string/starts-with? ?date "2026-")]
		        [(subs ?date 0 7) ?month]
		    ]
		    :view (fn [rows]
		      [:table {:style {:width "100%"}}
		        [:thead
		          [:tr
		            [:th {:style {:text-align "left" :padding "8px"}} "Месяц"]
		            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
		        [:tbody
		          (for [r (sort-by :month rows)]
		            [:tr
		              [:td {:style {:padding "8px"}} (:month r)]
		              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
		  }
		  #+END_QUERY
	- ### January
	  collapsed:: true
		- Месяц January 2026
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Jan 2026"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2026-01-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2026-01-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2026-01-01]]
		  id:: 3b9c9c6a-aab4-4a5a-a0f9-7c6bdd50173d
		  collapsed:: true
			- #food Матча
			  aud:: 8.40
		- [[2026-01-02]]
		  id:: b9ff2f32-d00c-4e7c-81a9-1727f0ff3dea
		  collapsed:: true
			- #shopping #ALDI Ice tea, бананы, сок, печенье, 2 энергетика
			  aud:: 19.45
			- #shopping #[[Woolworths]] 2 Цветы и сливки
			  aud:: 38
			- #service Массаж
			  aud:: 200
		- [[2026-01-03]]
		  id:: 11326469-45fd-4553-b555-c63d7629312f
		  collapsed:: true
			- #shopping #711 Очки, вода, 4 энергетика, шоколад
			  aud:: 57.10
			- #service #Larapinta Чекин кемпинг
			  aud:: 25
			- #food #Larapinta Чипсы
			  aud:: 2
		- [[2026-01-04]]
		  id:: 519a4d83-ec54-4bd2-bdfe-6151dfc252e9
		  collapsed:: true
			- #shopping #[[Coles]] 2 лимонада и шоколад
			  aud:: 13.50
			- #shopping #Mind-Games Карты, кубик и Huzzle
			  aud:: 60
			- #food #[[Goji Cafe]] Wrap
			  aud:: 21
		- [[2026-01-05]]
		  id:: c06459d5-3d21-4e0c-b1fb-bf96a3d8187c
		  collapsed:: true
			- #shopping #Australia-Fair Карты пазл и кубик
			  aud:: 39
			- #shopping #Choice Splat and Stick ball
			  aud:: 3
			- #shopping #[[ALDI]] Сок и 2 печенье
			  aud:: 11.25
			- #food #7-Eleven Энергетик
			  aud:: 3.50
		- [[2026-01-07]]
		  id:: a1e6a8af-111f-4411-9867-3ba278b3c0c8
		  collapsed:: true
			- #shopping #[[Coles]] Продукты - рис, хлеб, капли для носа, Quinoa Flakes, dates, сливки
			  aud:: 39.40
		- [[2026-01-08]]
		  id:: 55b8aad1-f687-4eaa-b525-ac0617467375
		  collapsed:: true
			- #shopping #[[Coles]] Бананы, сок, мыло, хумус, клей, печенье
			  aud:: 26.40
			- #shopping Спирт (Аптека)
			  aud:: 7.50
		- [[2026-01-09]]
		  id:: 086e3048-4824-43ee-873b-2ac930e18f22
		  collapsed:: true
			- #food #cafe Matcha с oat и пирожное
			  aud:: 11.70
			- #food Энергетик (Магазин)
			  aud:: 3.90
			- #food Энергетик (Магазин)
			  aud:: 4
			- #massage Nicole 1hour
			  aud:: 280
			- #shopping Arganine, Tulasi Tea
			  aud:: 69
			- #shopping #[[ALDI]] Ice tea, орешки, энергетик
			  aud:: 18.20
			- #shopping Оплата за чай с доставкой
			  aud:: 1066.25
		- [[2026-01-10]]
		  id:: ae1361e9-99e0-4d6c-92d5-f6ad57bf4b05
		  collapsed:: true
			- #food #cafe Tempura Rosti ([[Goji Cafe]])
			  aud:: 26.20
			- #food #cafe Matcha with Oat milk ([[Goji Cafe]])
			  aud:: 6
			- #Проекты Hostinger subscription (Baresma Makeb)
			  idr:: 918209
			- #IMAX Билет на Avatar
			  aud:: 39.30
			- #food #IMAX Cola and popcorn
			  aud:: 16.20
			- #food #711 2 энергетика, шоколад, вода
			  aud:: 14.60
			- #camping Ночевка Logan Park Farm
			  aud:: 25
			- #education Курс «Смысл»
			  usd:: 243
			  aud:: 363
		- [[2026-01-11]]
		  id:: b83a7575-4db3-4429-9625-5707da045a0c
		  collapsed:: true
			- #food #cafe Завтрак и Матча (Oaky Creek Farm)
			  aud:: 36
			- #shopping Кубик (Australia Fair)
			  aud:: 10
		- [[2026-01-12]]
		  id:: 14e93cba-58f3-496a-ae5c-ce7fffd43e68
		  collapsed:: true
			- #food #711 2 энергетика и сникерс
			  aud:: 14
			- #shopping Донейшн Хане на ветеренара
			  rub:: 10000
			  aud:: 192
			- #camping 2 Газ и сухое горючее (Bunnings)
			  aud:: 17
			- #subsription Domain kaqchikel.com
			  usd:: 22.19
			  aud:: 33
			- #shopping Ice tea, энергетик, Jamu, hot chocolate ([[Q Centre]])
			  aud:: 16.40
			- #shopping 2 цветы и печенье
			  aud:: 32.50
		- [[2026-01-13]]
		  id:: 723aab74-0c19-4109-871d-a126b61ce7ad
		  collapsed:: true
			- #food #[[Goji Cafe]] 2 Matcha with oat milk (Volunteering GC)
			  aud:: 12
			- #food #[[Goji Cafe]] Vegetarian wrap and Matcha with oat milk ([[Goji Cafe]])
			  aud:: 28.21
			- #subscription DeployHQ
			  idr:: 227000
			  aud:: 20.20
			- #subscription Telkomsel
			  idr:: 52000
		- [[2026-01-14]]
		  id:: 569383b7-2590-40c8-bf73-afedfde1becb
		  collapsed:: true
			- #car Депозит за машину (Budget Hire Car)
			  aud:: 100
			- #shopping #[[Coles]] Энергетик
			  aud:: 4
		- [[2026-01-15]]
		  id:: 80d4dd59-fe61-4d15-9bf2-939902c9eca4
		  collapsed:: true
			- #food #[[Goji Cafe]] Rosti Matcha with oat milk ([[Goji Cafe]])
			  aud:: 30.20
			- #food 2 энергетика и шоколад (711)
			  aud:: 10.35
		- [[2026-01-16]]
		  id:: cc518776-88c3-4347-870c-2b5ede66c004
		  collapsed:: true
			- #food #cafe Завтрак ([[Goji Cafe]])
			  aud:: 26.20
			- #service Массаж Gummy
			  aud:: 200
			- #food 2 энергетика и шоколад (711)
			  aud:: 10.25
			- #shopping Ice tea, энергетик, наклейки на нос #[[Coles]]
			  aud:: 37.75
		- [[2026-01-17]]
		  id:: e9002f98-23a6-488d-9657-46198a4e3abf
		  collapsed:: true
			- #shopping #amazon Худи НАСА и белая шапка Санты
			  aud:: 105.70
			- #subscription Claude
			  aud:: 170
		- [[2026-01-18]]
		  id:: a219f596-8824-4153-a7b9-2f11060a3da0
		  collapsed:: true
			- #shopping Лимонад, 2 энергетика, МнМс, освежитель (711)
			  aud:: 22.95
			- #food Лимонад ([[ASMY]])
			  aud:: 4
		- [[2026-01-19]]
		  id:: 172f6db0-92a7-4f7c-b5ea-418d101bc295
		  collapsed:: true
			- #food Завтрак #[[Goji Cafe]]
			  aud:: 27.20
			- #transactions PayPal to BCC
			  aud:: 7
			- #transactions Bcc 580 usd to 830 AUD in wise with
			  aud:: 45
			- #shopping #[[Woolworths]] Цветы, гороскоп на 2026, 2 печенья
			  aud:: 37.15
		- [[2026-01-20]]
		  id:: e8e7814b-80f1-46b9-883b-737604f6cc51
		  collapsed:: true
			- #food Завтрак и Матча #[[Goji Cafe]]
			  aud:: 26.20
			- #subscription #Amaysim
			  aud:: 30
			- #shopping Цветы
			  aud:: 72
			- #shopping #Choice Конверты
			  aud:: 3
			- #shopping #ALDI Ice tea печенье энергетик
			  aud:: 7.40
		- [[2026-01-21]]
		  id:: 0853522b-80b1-406f-8070-a918b5fe2c0c
		  collapsed:: true
			- #food Завтрак #[[Goji Cafe]]
			  aud:: 31.20
			- #shopping Лимонад и энергетик #[[ALDI]]
			  aud:: 4.60
		- [[2026-01-22]]
		  id:: 7ad65ed4-9edd-4b59-ac1a-880494043df0
		  collapsed:: true
			- #shopping Печенье Ice tea, енергетик #[[ALDI]]
			  aud:: 7.35
			- #shopping Бумажные стаканчики #Choice
			  aud:: 5
		- [[2026-01-23]]
		  id:: 76341293-d1a4-4862-9e6d-d54c60016964
		  collapsed:: true
			- #shopping Ice tea, Kit Kat #[[ALDI]]
			  aud:: 4.20
			- #health Массаж
			  aud:: 80
			- #health Массаж (доп)
			  aud:: 220
			- #food Пицца #PizzaHut
			  aud:: 5
		- [[2026-01-24]]
		  id:: c5a5bfeb-f708-4abd-ac57-b8a26e686912
		  collapsed:: true
			- #food Бургер, фри и вода
			  aud:: 19.50
			- #shopping Резинка #[[Coles]]
			  aud:: 2.50
			- #shopping Пазлы
			  aud:: 60
		- [[2026-01-25]]
		  id:: 79de491f-42e2-44cf-95c6-1959318999c5
		  collapsed:: true
			- #food Пицца #PizzaHut
			  aud:: 5
			- #food Кокосовая вода с кофе #PizzaHut
			  aud:: 5
		- [[2026-01-26]]
		  id:: d0c86925-6610-40ae-9fb0-cb848f7e3636
		  collapsed:: true
			- #shopping Мешочек для ключей
			  aud:: 1.5
			- #food Пицца #Dominos
			  aud:: 7
			- #shopping Цветы, печенье, ice tea, энергетик #[[ALDI]]
			  aud:: 17.55
		- [[2026-01-27]]
		  id:: 291e8a74-6d9b-4500-9d6d-a6a3d79ab339
		  collapsed:: true
			- #shopping Бензин #711
			  aud:: 79
			- #food Матча с Oat #[[Goji Cafe]]
			  aud:: 7.20
			- #food Матча и завтрак #Cw
			  aud:: 26.30
			- #shopping Стрижка #Barbershop
			  aud:: 35
			- #food Пуэр #Китайский-магазин
			  aud:: 14
			- #food Good Morning 2 #[[Goji Cafe]]
			  aud:: 2
			- #shopping Ice tea, v energy, печенье #[[ALDI]]
			  aud:: 7.40
			- #shopping Strum App
			  aud:: 30
		- [[2026-01-28]]
		  id:: b0e1fb0d-b007-498c-9c4a-2c44aa19c840
		  collapsed:: true
			- #food Завтрак и Матча с оат молоком #[[Goji Cafe]]
			  aud:: 32.10
			- #shopping Печенье, oat milk, v energy, ice tea #[[ALDI]]
			  aud:: 10.50
			- Брелок для ключей
			  aud:: 10
			- Махешику за февраль
			  idr:: 5500
		- [[2026-01-29]]
		  id:: 46ede4c0-532d-40fb-ac8e-fc9e7d8d50e7
		  collapsed:: true
			- subscription Claude Pro Max 20x
			  aud:: 231
			- #shopping Цветы и бутылка стеклянная для воды
			  aud:: 24.50
			- #shopping 3 карабина
			  aud:: 2.50
			- #shopping USB stick
			  aud:: 32
		- [[2026-01-30]]
		  id:: 979ac5be-fc10-4cbd-aa66-7f0766396b97
		  collapsed:: true
			- #food Асаи и матча #Goji
			  aud:: 22.50
			- #health Массаж [[GC Gummy]] утро
			  aud:: 200
			- #health Массаж [[GC Magi]] вечер
			  aud:: 270
		- [[2026-01-31]]
		  id:: 7eb19749-a74f-4a17-b8ef-745136c7fb4d
		  collapsed:: true
			- #food Mini coco fluff and Matcha with Oat milk [[Goji]]
			  aud:: 12
			- #shopping Принтер наклеек с телефона
			  aud:: 380
	- ### February
		- Месяц February 2026
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Feb 2026"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2026-02-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2026-02-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2026-02-01]]
		  id:: c51f44fd-c84a-4641-b671-ada36d799e79
		  collapsed:: true
			- #здоровье Массаж
			  aud:: 270
			- #food Пицца #[[Pizza Hut]]
			  aud:: 5.70
		- [[2026-02-02]]
		  id:: 0b9bb37a-41cc-4968-b671-ea1295018acf
		  collapsed:: true
			- #food Coconut coffee #[[Pizza Hut]]
			  aud:: 5
			- #food Pizza #[[Pizza Hut]]
			  aud:: 5
			- #shopping Шоколад и 2 энергетика #[[7-Eleven]]
			  aud:: 11
			- #shopping Энергетик, сливки, ice tea, подсластитель #[[Coles]]
			  aud:: 19.15
			- #обучение Social online course
			  aud:: 53
		- [[2026-02-03]]
		  id:: 1a9fce87-4351-4981-9e45-7bf978076be7
		  collapsed:: true
			- #transport Бензин #Заправка
			  aud:: 37.75
			- #shopping Ice tea, v energy, шоколад, 2 орехи, молоко #[[ALDI]]
			  aud:: 38.20
			- #shopping Шоколад цветы #[[Woolworths]]
			  aud:: 20.50
			- #подписка Civitai subscription 1 month
			  aud:: 15
		- [[2026-02-04]]
		  id:: bf6224cf-a93e-4212-8cf2-c35ac623a2cd
		  collapsed:: true
			- #food Tempura Me and Matcha with Oat Milk #[[Goji Cafe]]
			  aud:: 31.20
			- #shopping Solo energy #[[Choice]]
			  aud:: 3
		- [[2026-02-05]]
		  id:: 6337d090-b872-4023-8055-dbbe3fa5e5fa
		  collapsed:: true
			- #food Завтрак #[[Goji Cafe]]
			  aud:: 27.20
			- #food Burrito and Chai #[[Guzman and Gomez]]
			  aud:: 19.50
			- #shopping Шоколад, v energy, ice tea #[[ALDI]]
			  aud:: 8.05
			- #transport Бензин #Заправка
			  aud:: 12.50
			- #shopping GoCube
			  aud:: 105
		- [[2026-02-06]]
		  id:: 80c16455-7105-47bd-ac01-14e8671b4dbe
		  collapsed:: true
			- #food Бурито и лате #[[Guzman and Gomez]]
			  aud:: 16.70
			- #shopping Энергетик и шоколад #[[Coles]]
			  aud:: 8.20
		- [[2026-02-07]]
		  id:: c500084f-32e9-48a3-9479-1ec7b1a4577b
		  collapsed:: true
			- #food Quesadilla and tea #[[Guzman y Gomez]]
			  aud:: 15.20
			- #shopping 2 печенье, энергетик, ice tea #[[ALDI]]
			  aud:: 10.15
		- [[2026-02-08]]
		  id:: cf7e22c5-b3a7-4344-b54d-66a9dd86535a
		  collapsed:: true
			- #food Big Bur Shitake, Hash Brown, Med Latte #[[Guzman y Gomez]]
			  aud:: 18.70
			- #shopping Губная гармошка #[[Музыкальный Магазин]]
			  aud:: 50
			- #shopping NMN #[[Аптека]]
			  aud:: 90
			- #shopping Вода #[[Аптека]]
			  aud:: 4
		- [[2026-02-09]]
		  id:: 4cb3f3e3-95be-4939-9c73-838f6e5b3847
		  collapsed:: true
			- #food Tacos #[[Guzman y Gomez]]
			  aud:: 14.70
			- #shopping 2 энергетика и печенье #711
			  aud:: 11.90
			- #здоровье Массаж
			  aud:: 270
			- #food Пицца #[[Pizza Hut]]
			  aud:: 5
			- #food Бутылка воды #[[Pizza Hut]]
			  aud:: 2
		- [[2026-02-10]]
		  id:: 771b1617-cac1-401e-8adf-e9302a786fde
		  collapsed:: true
			- #shopping 2 энергетика и шоколад #711
			  aud:: 10.75
			- #shopping Носки и лакрица #[[Woolworths]]
			  aud:: 18.75
		- [[2026-02-11]]
		  id:: 745894ba-b833-4605-9452-a88a05d3d24c
		  collapsed:: true
			- #transport Заправка #Заправка
			  aud:: 36
			- #shopping 2 энергетика и шоколад #711
			  aud:: 10.10
			- #shopping Arganin #[[Health shop]]
			  aud:: 72.10
			- #shopping Цитрулин #[[Health shop]]
			- #shopping Аромат для машины #711
			  aud:: 4.95
		- [[2026-02-12]]
		  id:: d65b0807-9464-422e-a33f-86dc89f34a17
		  collapsed:: true
			- #transport Бензин #Заправка
			  aud:: 85
			- #food Кокосовая вода с кофе
			  aud:: 5
			- #shopping Гитара #[[Cash Converters]]
			  aud:: 650
			- #food Обед и кофе #GYG
			  aud:: 16.70
			- #shopping Цепочка для кошелька #Choice
			  aud:: 2
		- [[2026-02-13]]
		  id:: ae31a9ce-f3a7-44cb-8887-1357656aa3be
		  collapsed:: true
			- #food Матча с оат милк
			  aud:: 6.40
		- [[2026-02-14]]
		  id:: ba4fecf7-b12d-478f-819e-e19a7f810a7e
		  collapsed:: true
			- #food Пицца
			  aud:: 25
		- [[2026-02-16]]
		  id:: ac43bf47-f453-4599-b031-abb6052fdaeb
		  collapsed:: true
			- #health Массаж
			  aud:: 80
			- #health Массаж с [[ASMY-Emma]]
			  aud:: 200
			- #food Кокосовая вода #[[Pizza Hut]]
			  aud:: 5
			- #food Пицца #[[Pizza Hut]]
			  aud:: 5
			- #shopping Ice tea, 2 печенье, энергетик #[[ALDI]]
			  aud:: 10.25
		- [[2026-02-17]]
		  id:: fbce646d-7543-4051-96e9-e0f7e73fd09a
		  collapsed:: true
			- #infrastructure VPS to Sydney #VPS
			  aud:: 60
			- #infrastructure Домен PRIVOROT-GADANIE.COM за год
			  aud:: 74.03
		- [[2026-02-18]]
		  id:: 3ef3c190-3fc3-42c3-a9dc-565964c2b613
		  collapsed:: true
			- #food Завтрак и латте #[[GYG]]
			  aud:: 16.20
			- #food Пицца #[[Pizza Hut]]
			  aud:: 5
			- #food Кокосовая вода
			  aud:: 5
		- [[2026-02-19]]
		  id:: 65846b6b-2d41-4f9e-ad19-9a9c6656f0d0
		  collapsed:: true
			- #fee Комиссия за перевод
			  aud:: 35
			- #hardware Монитор
			  aud:: 148
			- #music Струны
			  aud:: 70
			- #food Пицца
			  aud:: 25
		- [[2026-02-20]]
		  id:: 1e0aef00-650a-41a7-a3a7-3e183b16fbc2
		  collapsed:: true
			- #shopping Кабель для зарядки от Power Bank
			  aud:: 25
		- [[2026-02-21]]
		  id:: 9c568248-2c05-4f30-8683-c76ce0044b90
		  collapsed:: true
			- #shopping 2 шоколадки, вода, 2 энергетика
			  aud:: 21.40
			- #food Чипсы
			  aud:: 7.50
			- #travel Кемпинг
			  aud:: 25
		- [[2026-02-22]]
		  id:: b680cfcf-60cd-4e38-8001-0faad86cb3cf
		  collapsed:: true
			- #shopping Оборудование для гитары
			  rub:: 2990
			- #income ЗП 20 февраля
			  aud:: 500
			- #income ЗП CRM
			  rub:: 2990
			- #shopping Энергетик 473ml
			  aud:: 7.20
			- #food Блины с капучино
			  aud:: 7.50
			- #transport Бензин #[[Заправка]]
			  aud:: 80.30
			- #food Пицца
			  aud:: 5.70
			- #food Лимонад
			  aud:: 3
			- #food Сладости charity
			  aud:: 4
		- [[2026-02-23]]
		  id:: 80e1030c-67f8-4686-ace6-a3a03f59dd4c
		  collapsed:: true
			- #shopping 2 цветы и 2 сливки #Woolworths
			  aud:: 42
			- #food Kava
			  aud:: 70
			- #shopping Pine Bark #[[Flannerys Robina]]
			  aud:: 20
			- #shopping Лимонад из кокоса #[[Flannerys Robina]]
			  aud:: 4
		- [[2026-02-24]]
		  id:: 99d80858-879d-45d1-825c-5d2d49a30083
		  collapsed:: true
			- #food Завтрак #[[GYG]]
			  aud:: 11.60
			- #food Драник и гукамоле
			  aud:: 4.70
			- #shopping 2 энергетика, ice tea, хлеб, 2 печенье, oat milk #[[ALDI]]
			  aud:: 17.30
		- [[2026-02-25]]
		  id:: c8bf88e8-4a5e-4d53-b764-f09499fd5e87
		  collapsed:: true
			- #food Сандвич и чай
			  aud:: 25.50
		- [[2026-02-26]]
		  id:: 4f1d540e-5d8c-4a02-ae21-87959d11ebfb
			- #food Ice tea, 2 timtam, печенье, какао, кофе
			  aud:: 33.50
		- [[2026-02-27]]
		  id:: ebe2cc28-a9c7-4a58-bb44-e2dfef8aadfe
			- #food Энергетик 500ml
			  aud:: 6
			- #food Пицца
			  aud:: 5
			- #food Лимонад
			  aud:: 3.10
			- #food Vegetarian Kebab
			  aud:: 18.50
			- #food Лимонад и шоколад
			  aud:: 4.60
			- #food Чай dandelion
			  aud:: 13
			- #shopping Haircut
			  aud:: 37
	- ### March
	  collapsed:: true
		- Месяц March 2026
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Mar 2026"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2026-03-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- [[2026-03-01]]
		  id:: a0b1c2d3-e4f5-6789-abcd-ef1234567890
		  collapsed:: true
			- #shopping Миндаль, кешью, ромашка
			  aud:: 69.30
			- #shopping 2 энергетика и шоколад
			  aud:: 18.30
			- Subscription Claude Code Max 20x
			  aud:: 309
			- [[ASMY]] membership
			  aud:: 250
		- [[2026-03-04]]
		  id:: d4e5f304-0304-4304-8304-030420260304
		  collapsed:: true
			- #food 2 энергетика и шоколад #[[711]]
			  aud:: 11.20
			- Занятие табла
			  aud:: 65
			- Рукописи на Санскрите
			  rub:: 4800
		- [[2026-03-05]]
		  id:: e5f60305-0305-4305-8305-030520260305
		  collapsed:: true
			- Subscription privorot-help.com
			  aud:: 76.50
			- #shopping 2 энергетика и шоколад #[[7-Eleven]]
			  aud:: 14.50
			- #shopping Заправка #[[7-Eleven]]
			  aud:: 20
			- #shopping Стекло и батарея на телефон
			  aud:: 180
			- #shopping Подставка в машину
			  aud:: 29
			- Subscription [[Прем Баба]]
			  aud:: 52
		- [[2026-03-06]]
		  id:: f6a70306-0306-4306-8306-030620260306
		  collapsed:: true
			- #food 2 энергетика и шоколад #[[711]]
			  aud:: 11.20
			- #shopping 3 печенья, энергетик, ice tea, banana #[[ALDI]]
			  aud:: 14.60
			- #food Обед #[[GYG]]
			  aud:: 17
			- NextClinic e-script
			  aud:: 50
			- Sildenafil #[[Chemist Warehouse]]
			  aud:: 45
			- #shopping Water
			  aud:: 2.60
			- Shishi massage
			  aud:: 200
			- #food Veggie Wrapper #[[Hungry Jack's]]
			  aud:: 10.50
			- #shopping Бензин
			  aud:: 103.90
		- [[2026-03-07]]
		  id:: c8d9e0f1-a2b3-4567-cdef-012345678901
		  collapsed:: true
			- #food Avocado roll
			  aud:: 4.50
		- [[2026-03-09]]
		  id:: f8c1e0g2-b3c4-5678-defg-123456789012
		  collapsed:: true
			- #shopping 2 энергетика и мороженое
			  aud:: 12.50
			- #shopping 2 энергетика
			  aud:: 7
			- #shopping Цветы, кофе
			  aud:: 23
		- [[2026-03-10]]
		  id:: 9c2f1h3i-c4d5-6789-efgh-234567890123
		  collapsed:: true
			- #food Буррито с кофе
			  aud:: 15
			- #shopping 2 кабеля для зарядки iPhone
			  aud:: 50
			- #shopping Сок и шоколад
			  aud:: 7.25
			- #food Пицца
			  aud:: 25
		- [[2026-03-11]]
		  id:: b2c3d4e5-f6a7-8901-bcde-fa2345678901
		  collapsed:: true
			- #food Пицца #[[Pizza Hut]]
			  aud:: 5
			- #food Кокос с кофе
			  aud:: 5
			- Табласы
			  rub:: 700
			- #shopping Тальк
			  aud:: 6.50
			- Перевод Бендиго в кэш
			  aud:: 200
		- [[2026-03-12]]
		  id:: c3d4e5f6-a7b8-9012-cdef-0b2345678901
		  collapsed:: true
			- #food Обед quesadilla и кофе
			  aud:: 15.50
			- #food 2 энергетика
			  aud:: 7
		- [[2026-03-13]]
		  id:: d4e5f6a7-b8c9-0123-def0-1c2345678901
		  collapsed:: true
			- #shopping 2 энергетика и шоколад
			  aud:: 12.50
			- #food Завтрак #GYG
			  aud:: 19.50
			- #food Chamomile tea #Goldie's
			  aud:: 4.50
		- [[2026-03-14]]
		  id:: e5f6a7b8-c9d0-1234-ef01-2d3456789012
		  collapsed:: true
			- #shopping Шоколад
			  aud:: 8
			- #shopping 2 энергетика
			  aud:: 7
		- [[2026-03-15]]
		  id:: f6a7b8c9-d0e1-2345-f012-3e4567890123
		  collapsed:: true
			- #shopping 2 энергетика
			  aud:: 7
			- #app Rhythm App
			  aud:: 9
		- [[2026-03-16]]
		  id:: a7b8c9d0-e1f2-3456-0123-4f5678901234
		  collapsed:: true
			- #maps Australia map
			  aud:: 13
			- #food Brownie and Tea
			  aud:: 19.50
		- [[2026-03-17]]
		  collapsed:: true
			- Энергетик
			  aud:: 3
			- Subscription Suno
			  aud:: 38
			- Arganin и чай Тулси
			  aud:: 93.75
			- Фалафель и фанта
			  aud:: 18.10
			- NutriBullet и энергетик
			  aud:: 83.50
		- [[2026-03-18]]
		  collapsed:: true
			- Book
			  aud:: 40
			- Энергетик
			  aud:: 2.70
			- Энергетик
			  aud:: 2
			- Amaysim
			  aud:: 30
			- Обед
			  aud:: 16.20
			- Энергетик и шоколад
			  aud:: 6.50
			- Энергетик
			  aud:: 3
			- Таблы
			  aud:: 173
			- Бензин
			  aud:: 112.75
			- Кэроб
			  aud:: 5
		- [[2026-03-19]]
		  collapsed:: true
			- Сендвич
			  aud:: 12.90
			- Энергетик
			  aud:: 6
			- Бурито и ice tea
			  aud:: 16.20
			- Шоколад и орехи
			  aud:: 17.50
		- [[2026-03-20]]
		  collapsed:: true
			- Матча и пирожное
			  aud:: 15.50
			- Завтрак
			  aud:: 16.20
			- 4 энергетика
			  aud:: 4
			- Обед
			  aud:: 20.50
			- Энергетик и шоколад
			  aud:: 5.10
			- subscription Prem Baba
			  aud:: 53
		- [[2026-03-21]]
		  collapsed:: true
			- Meditation Seminar
			  aud:: 27
			- Burrito
			  aud:: 11
			- Энергетик и шоколад
			  aud:: 9.50
		- [[2026-03-22]]
		  collapsed:: true
			- Десерт
			  aud:: 9
			- Шоколад
			  aud:: 2.50
		- [[2026-03-23]]
		  collapsed:: true
			- Donation Vera
			  aud:: 100
			- 4 энергетика и шоколад
			  aud:: 10.10
			- Обед
			  aud:: 11
		- [[2026-03-24]]
		  collapsed:: true
			- Шоколад
			  aud:: 4
			- Энергетик
			  aud:: 4.60
			- Шоколад и 4 энергетик
			  aud:: 9.5
			- Буррито и мил
			  aud:: 22
		- [[2026-03-25]]
		  collapsed:: true
			- Завтрак
			  aud:: 14.20
			- Лате
			  aud:: 4
			- Печенье
			  aud:: 3.60
			- Обед
			  aud:: 15.40
			- Пластырь от мозоли
			  aud:: 13
		- [[2026-03-26]]
		  collapsed:: true
			- Энергетики и шоколад
			  aud:: 11.75
			- Ginger ninja and snickers
			  aud:: 7
			- Стрижка и бритье
			  aud:: 72
			- Обед
			  aud:: 15.70
			- Шоколад
			  aud:: 4
			- 2 чипсы и шоколад
			  aud:: 17
		- [[2026-03-27]]
		  collapsed:: true
			- Сок и шоколад
			  aud:: 7
			- 4 энергетика
			  aud:: 4
			- Обед
			  aud:: 14.20
			- Churros
			  aud:: 4
			- subscription useapi
			  aud:: 23
		- [[2026-03-28]]
		  collapsed:: true
			- Массаж
			  aud:: 280
			- 2 энергетика
			  aud:: 7
			- Шоколад
			  aud:: 9
			- Курсы НЛП и Гипноз
			  aud:: 54
			- Курсы Английского
			  aud:: 127
			- Шоколад
			  aud:: 3.50
			- Курс по Английскому только
			  aud:: 60
			- Только
			  aud:: 40
		- [[2026-03-29]]
		  collapsed:: true
			- Органик чипсы
			  aud:: 3.80
			- Шоколад с мятой
			  aud:: 3
			- Энергетик
			  aud:: 4.50
		- [[2026-03-30]]
		  collapsed:: true
			- Энергетик и шоколад
			  aud:: 4.25
			- 4 энергетика и мятный шоколад
			  aud:: 9
			- Обед
			  aud:: 15.50
			- за жильё
			  aud:: 350
		- [[2026-03-31]]
		  collapsed:: true
			- 2 энергетика и шоколад
			  aud:: 18.50
			- Шоколадки и 4 энергетика
			  aud:: 9.50
			- Обед Начос
			  aud:: 16.40
			- Ретрит
			  aud:: 750
	- ### April
	  collapsed:: true
		- Месяц April 2026
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Apr 2026"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2026-04-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?day (sum ?n)
			      :keys day aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2026-04-")]
			        [(subs ?date 5) ?day]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "День"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :day rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:day r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2026-04-01]]
		  collapsed:: true
			- Энергетик
			  aud:: 2.75
			- Claude Max 20x
			  aud:: 330
			- Энергетик
			  aud:: 2.75
			- Энергетик
			  aud:: 2.75
		- [[2026-04-02]]
		  collapsed:: true
			- 2 энергетика
			  aud:: 7
			- Энергетик
			  aud:: 2
			- Энергетик
			  aud:: 2
			- Бензин
			  aud:: 117.75
			- Обед
			  aud:: 15.40
		- [[2026-04-04]]
		  collapsed:: true
			- 4 энергетика и сникерс
			  aud:: 13.50
			- Кабель
			  aud:: 17
		- [[2026-04-05]]
		  collapsed:: true
			- Курс
			  aud:: 7
			- Карты оракул
			  aud:: 24
		- [[2026-04-06]]
		  collapsed:: true
			- 4 энергетика и скотч
			  aud:: 15.25
		- [[2026-04-07]]
		  collapsed:: true
			- Энергетик
			  aud:: 2.75
			- Энергетик
			  aud:: 2.75
			- Обед мини бурито и айс ти
			  aud:: 16.20
			- Зубная паста
			  aud:: 5.60
			- Цветы
			  aud:: 15
		- [[2026-04-11]]
		  collapsed:: true
			- Массаж
			  aud:: 200
			- #shopping Шоколад и энергетик #711
			  aud:: 9.25
		- [[2026-04-13]]
		  collapsed:: true
			- подписка DeployHQ
			  aud:: 23
			- #shopping Шоколад и 2 энергетика #711
			  aud:: 18
			- #food Матча #GojiBakeryCafe
			  aud:: 6.70
			- #shopping Энергетик #Coles
			  aud:: 2
			- #food Обед #GYG
			  aud:: 15
			- #shopping Ice tea и 4 энергетика #ALDI
			  aud:: 6
		- [[2026-04-18]]
		  collapsed:: true
			- #shopping 6 шоколадок #711
			  aud:: 3
		- [[2026-04-19]]
		  collapsed:: true
			- #food Завтрак
			  aud:: 44
		- [[2026-04-21]]
		  collapsed:: true
			- #shopping Энергетик #Coles
			  aud:: 2.75
			- #shopping Энергетик #Coles
			  aud:: 4.50
			- #shopping Шоколад, лакрица и энергетик #Coles
			  aud:: 11
			- #food Обед #GYG
			  aud:: 12.5
			- #shopping Бензин
			  aud:: 98.70
		- [[2026-04-22]]
		  collapsed:: true
			- #shopping Энергетик
			  aud:: 2.75
			- #shopping Энергетик
			  aud:: 2.75
			- #food Пирожок #BakersDelight
			  aud:: 4.20
			- #shopping Oat milk
			  aud:: 2
			- #shopping Oat milk
			  aud:: 2
			- #food Пирожок #BakersDelight
			  aud:: 4.20
			- #food Spinach and feta danish #BakersDelight
			  aud:: 0
			- #shopping 2 шоколадки и 2 энергетика #711
			  aud:: 13.60
		- [[2026-04-23]]
		  collapsed:: true
			- #shopping Кофе и печенье #711
			  aud:: 3
			- #shopping Almond milk #Coles
			  aud:: 2
			- #shopping Spinach and feta danish #Coles
			  aud:: 4.20
			- #shopping Oat milk #Coles
			  aud:: 2
			- #shopping Spinach and feta danish #Coles
			  aud:: 4.20
			- #shopping Шоколад и кофе #IGA
			  aud:: 15.24
			- #food Обед #GYG
			  aud:: 14.90
		- [[2026-04-24]]
		  collapsed:: true
		  aud:: 116.80
			- #shopping Кофе
			  aud:: 4.5
			- #shopping Spinach and feta danish #Coles
			  aud:: 4.20
			- #shopping Oat milk #Coles
			  aud:: 2
			- #shopping 2 энергетика и 2 шоколада
			  aud:: 17.40
			- #shopping Sauna
			  aud:: 69
			- #shopping Чипсы
			  aud:: 4.80
			- #food Обед #GYG
			  aud:: 14.90
		- [[2026-04-25]]
		  collapsed:: true
			- #shopping 2 шоколадки и энергетик #711
			  aud:: 13.40
			- #shopping Фанта и шоколад
			  aud:: 7.30
			- #shopping Шоколад и 2 энергетика #711
			  aud:: 13.50
		- [[2026-04-26]]
		  collapsed:: true
			- #shopping Кокосовая вода, кефир, кофе и шоколад #IGA
			  aud:: 35.20
			- #shopping Carb
			  aud:: 276
			- #food Леманад #ASMY
			  aud:: 4
			- #shopping Подписка [[Прем Баба]]
			  aud:: 50
		- [[2026-04-27]]
		  collapsed:: true
			- #shopping Энергетик #Coles
			  aud:: 2.75
			- #shopping 3 кокосовая вода и 1 энергетик #Iga
			  aud:: 12.50
			- #food Мил #HungryJack
			  aud:: 13.90
			- #shopping Сок #Coles
			  aud:: 3.30
			- #food Мил #HungryJack
			  aud:: 13.90
		- [[2026-04-28]]
		  collapsed:: true
			- #shopping Oat milk #Coles
			  aud:: 2
			- #shopping Spinach and feta danish #Coles
			  aud:: 4.20
			- #shopping Энергетик #Coles
			  aud:: 4.45
			- #shopping Стрижка #Barbershop
			  aud:: 47
			- #food Обед #GYG
			  aud:: 14.90
			- #shopping Бананы, печенье, ice tea #ALDI
			  aud:: 10.80
			- OpenClaw MasterClass
			  aud:: 40
		- [[2026-04-29]]
		  collapsed:: true
			- #shopping Oat milk и энергетик #Coles
			  aud:: 6.45
			- #shopping Mediterranean pizza #Woolworths
			  aud:: 5.30
			- #shopping Шоколад и энергетик
			  aud:: 10.75
		- [[2026-04-30]]
		  collapsed:: true
			- #shopping Энергетик #Coles
			  aud:: 4.75
			- #shopping Oat milk
			  aud:: 2
			- #shopping Spinach and feta danish
			  aud:: 4.20
			- #shopping 4 энергетика, 5 шоколада и кешью #ALDI
			  aud:: 24.50
			- #food Обед с латте #GYG
			  aud:: 14.90
			- #shopping SSD и RAM
			  aud:: 1650
	- ### May
	  collapsed:: true
		- Месяц May 2026
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD May 2026"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2026-05-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?day (sum ?n)
			      :keys day aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2026-05-")]
			        [(subs ?date 5) ?day]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "День"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :day rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:day r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2026-05-01]]
		  collapsed:: true
			- #subscription Claude Max
			  aud:: 340
			- #shopping Энергетик #Coles
			  aud:: 2.75
			- #food Обед с латте #GYG
			  aud:: 14.90
			- #shopping Шоколад #ALDI
			  aud:: 3
			- #subscription NextClinic eScript
			  aud:: 39.90
		- [[2026-05-03]]
		  collapsed:: true
			- #subscription Mannix
			  aud:: 243
			- #shopping 2 энергетика и шоколад #711
			  aud:: 8.70
		- [[2026-05-02]]
		  collapsed:: true
			- #shopping Энергетик и шоколад
			  aud:: 12.95
			- #shopping Бензин #BP
			  aud:: 91.15
			- #shopping Энергетик #BP
			  aud:: 4.30
		- [[2026-05-04]]
		  collapsed:: true
			- #shopping 2 энергетика и шоколад #711
			  aud:: 13.50
			- #shopping Ромашка
			  aud:: 4.20
			- #shopping Глютен фри хлеб и шоколад #Organic
			  aud:: 19
			- #shopping Сильденафил #Аптека
			  aud:: 45
		- [[2026-05-05]]
		  collapsed:: true
			- #shopping Рыбий жир и энергетик #Coles
			  aud:: 29.20
			- #food Обед
			  aud:: 14
			- #shopping Энергетик #Woolworths
			  aud:: 3.90
			- #shopping Чай, Арганини #Аптека
			  aud:: 88
		- [[2026-05-06]]
		  collapsed:: true
			- #shopping 3 кокосовой воды #Coles
			  aud:: 8.60
			- #food Spinach and feta danish
			  aud:: 4.20
			- #food Spinach and feta danish
			  aud:: 4.20
		- [[2026-05-07]]
		  collapsed:: true
			- #shopping Аренда коврика #ASMY
			  aud:: 2
			- #shopping Сауна #ASMY
			  aud:: 39
			- #shopping Кокосовая вода #Coles
			  aud:: 3.30
			- #shopping Вода
			  aud:: 4.10
			- #food Burrito
			  aud:: 10.90
		- [[2026-05-08]]
		  collapsed:: true
			- #shopping Oat milk #Coles
			  aud:: 2
			- #food Spinach and feta danish
			  aud:: 4.20
			- #food Обед с колой
			  aud:: 16.20
		- [[2026-05-09]]
		  collapsed:: true
			- #shopping 2 шоколадки и энергетик #711
			  aud:: 16.45
		- [[2026-05-10]]
		  collapsed:: true
			- #shopping 2 энергетика и шоколад #711
			  aud:: 11.70
		- [[2026-05-11]]
		  collapsed:: true
			- #food Матча #[[Goji Cafe]]
			  aud:: 6.20
			- #shopping Oat milk
			  aud:: 2
			- #shopping Spinach and feta danish
			  aud:: 4.20
			- #shopping Cola #Coles
			  aud:: 4.45
			- #food Обед
			  aud:: 20.30
			- #shopping Лимонад, печенье и энергетик #Coles
			  aud:: 14.70
		- [[2026-05-12]]
		  collapsed:: true
			- #shopping Баня #ASMY
			  aud:: 39
			- #shopping Матча #Coles
			  aud:: 4.90
			- #education Dan Bilzerian's Optimal Game System
			  aud:: 25
			- #shopping Шоколад, сок и 2 кокосовая вода #IGA
			  aud:: 27.20
			- #food Обед #GYG
			  aud:: 21.50
		- [[2026-05-13]]
		  collapsed:: true
			- #food Матча
			  aud:: 5.50
			- #food Матча
			  aud:: 6.30
			- #shopping Вода
			  aud:: 4.30
			- #shopping Конверты
			  aud:: 3
			- Bendigo to cash 400 AUD
			- #telecom Amaysim
			  aud:: 30
			- #shopping Вода
			  aud:: 4.30
			- #food Matcha
			  aud:: 4.90
			- #housing Аренда комнаты
			  aud:: 350
			- #education Табла уроки
			  aud:: 250
		- [[2026-05-14]]
		  collapsed:: true
			- #food Матча и шоколад
			  aud:: 11.90
			- #shopping Матча и шоколад [[Coles]]
			  aud:: 11.90
		- [[2026-05-15]]
		  collapsed:: true
			- #shopping Лимонад и шоколад [[Coles]]
			  aud:: 7.95
			- #shopping Шоколад [[Coles]]
			  aud:: 6
		- [[2026-05-16]]
		  collapsed:: true
			- #shopping Жвачка
			  aud:: 2.50
			- #health Массаж
			  aud:: 80
			- #health Массаж
			  aud:: 200
			- #food Чай
			  aud:: 4.50
			- #food Мини пицца
			  aud:: 6
			- #food Матча
			  aud:: 6.20
			- #shopping Кола и шоколад
			  aud:: 12.20
		- [[2026-05-17]]
		  collapsed:: true
			- #food Кола и шоколад
			  aud:: 17.50
		- [[2026-05-18]]
		  collapsed:: true
			- #shopping Матча, наклейки на нос, 2 шоколада #Coles
			  aud:: 44.50
		- [[2026-05-19]]
		  collapsed:: true
			- #shopping Баня #ASMY
			  aud:: 39
			- #food Кокосовая вода, шоколад, кола, вода #Agi
			  aud:: 22.45
			- #food Обед #[[Tokyo Cafe]]
			  aud:: 18
			- #food Чай #[[Tokyo Cafe]]
			  aud:: 4
			- #food Лимонад #[[Tokyo Cafe]]
			  aud:: 3.50
			- #shopping Кокосовая вода и шоколад #Coles
			  aud:: 9
		- [[2026-05-20]]
		  collapsed:: true
			- #food Обед
			  aud:: 31.25
			- #food Сок
			  aud:: 7
		- [[2026-05-21]]
		  collapsed:: true
			- #education БГ с Ушей
			  aud:: 120
			- #shopping Лимонад с шоколадом
			  aud:: 14.30
			- #shopping Шоколад и матча #Coles
			  aud:: 13.90
		- [[2026-05-22]]
		  collapsed:: true
			- #food Матча
			  aud:: 4.90
			- #shopping Орешки
			  aud:: 14
		- [[2026-05-23]]
		  collapsed:: true
			- #food Лимонад и шоколад
			  aud:: 7.40
		- [[2026-05-24]]
		  collapsed:: true
			- #shopping Лимонад и печенье
			  aud:: 10
			- #shopping Лимонад
			  aud:: 5.70
		- [[2026-05-25]]
		  collapsed:: true
			- #shopping Лимонад #711
			  aud:: 4
			- #shopping Oat milk #Coles
			  aud:: 2
			- #shopping Spinach and feta danish #Coles
			  aud:: 4.40
			- #shopping Лимонад и шоколад #Coles
			  aud:: 11.50
		- [[2026-05-26]]
		  collapsed:: true
			- #food Сок и шоколад #Coles
			  aud:: 8.95
			- #food Буррито с фри и колой #GYG
			  aud:: 5.80
		- [[2026-05-27]]
		  collapsed:: true
			- #subscription Openrouter
			  usd:: 16
			- #shopping Вода [[Coles]]
			  aud:: 0.80
	- [[2026-05-28]]
	  collapsed:: true
		- #shopping Вода и хлеб #Coles
		  aud:: 6.60
		- #shopping Бензин
		  aud:: 81.70
		- #education Wing Girl Method
		  usd:: 65
	- [[2026-05-29]]
	  collapsed:: true
		- #shopping Энергетик #Coles
		  aud:: 2.75
		- #shopping Энергетик #Coles
		  aud:: 2.75
		- #shopping Шоколад и энергетик
		  aud:: 9.25
	- [[2026-05-30]]
	  collapsed:: true
		- #shopping Лимонад и МнМс #711
		  aud:: 14.30
	- [[2026-05-31]]
	  collapsed:: true
		- #Учёба Курс с управлениями для стойки на руках
		  aud:: 24
	- ### June
	  collapsed:: true
		- Месяц June 2026
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD June 2026"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2026-06-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?day (sum ?n)
			      :keys day aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2026-06-")]
			        [(subs ?date 5) ?day]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "День"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :day rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:day r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2026-06-01]]
		  collapsed:: true
			- #subscription Claude 340
			  aud:: 340
			- #shopping Энергетик #Coles
			  aud:: 2.75
			- #shopping Энергетик #Coles
			  aud:: 4.45
			- #shopping Энергетик
			  aud:: 3.45
			- #food Cheesymite
			  aud:: 4.10
			- #shopping Хлеб и шоколад
			  aud:: 13.70
			- #shopping Цветы
			  aud:: 35
			- #food Чай
			  aud:: 25
			- #subscription Yobu
			  aud:: 25
			- #subscription Seeking
			  aud:: 165
- ## 2025
  collapsed:: true
	- Год 2025
	  collapsed:: true
		- #+BEGIN_QUERY
		  {
		    :title [:p "AUD 2025"]
		    :query [
		      :find (sum ?n)
		      :with ?b
		      :where
		        [?b :block/properties ?prop]
		        [(get ?prop :aud) ?v]
		        [(* 1 ?v) ?n]
		        [?b :block/parent ?parent]
		        [?parent :block/refs ?ref]
		        [?ref :block/name ?name]
		        [(clojure.string/starts-with? ?name "2025-")]
		    ]
		    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
		  }
		  #+END_QUERY
	- По месяцам
	  collapsed:: true
		- collapsed:: true
		  #+BEGIN_QUERY
		  {
		    :title [:p "AUD по месяцам 2025"]
		    :query [
		      :find ?month (sum ?n)
		      :keys month aud
		      :where
		        [?b :block/properties ?prop]
		        [(get ?prop :aud) ?v]
		        [(* 1 ?v) ?n]
		        [?b :block/parent ?parent]
		        [?parent :block/refs ?ref]
		        [?ref :block/name ?date]
		        [(clojure.string/starts-with? ?date "2025-")]
		        [(subs ?date 0 7) ?month]
		    ]
		    :view (fn [rows]
		      [:table {:style {:width "100%"}}
		        [:thead
		          [:tr
		            [:th {:style {:text-align "left" :padding "8px"}} "Месяц"]
		            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
		        [:tbody
		          (for [r (sort-by :month rows)]
		            [:tr
		              [:td {:style {:padding "8px"}} (:month r)]
		              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
		  }
		  #+END_QUERY
	- ### May
	  collapsed:: true
		- Месяц May 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD May 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-05-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-05-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-05-24]]
		  id:: 9289ac74-fdb7-4ae0-8f33-f30b4d7de3de
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 16500
			- #laundry
			  idr:: 22500
			- #taxi #Adi-House-Moding
			  idr:: 24500
			- #shopping по пути в [[Adi House Moding]]
			  idr:: 69000
		- [[2025-05-25]]
		  id:: 9281162a-19cb-4d54-ac81-6ad8e665336c
		  collapsed:: true
			- #food #delivery
			  idr:: 68600
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Cocoku #Adi-House-Moding
			  idr:: 16000
			- #shopping #Cocoku - Печенье, бананы
			  idr:: 98150
		- [[2025-05-27]]
		  id:: dbc61a2a-6a09-4b28-b6b4-8549597d51b8
		  collapsed:: true
			- #food #delivery
			  idr:: 100800
			- #taxi #Tuta-House
			  idr:: 10500
			- #taxi #Adi-House-Moding
			  idr:: 0
			- **Доходы**
			- Комиссия за перевод на PayPal 20 USDT
		- [[2025-05-28]]
		  id:: 6ab6c6cc-201d-42a3-9837-57416e641b6a
		  collapsed:: true
			- #taxi #Tuta-House
			  idr:: 12000
			- #taxi #Adi-House-Moding
			  idr:: 13500
			- #book Самооценка
			  idr:: 84000
			- #вода
			  idr:: 26000
			- #taxi #Tuta-House
			  idr:: 13500
			- #taxi #Adi-House-Moding
			  idr:: 12000
		- [[2025-05-29]]
		  id:: f51ffc3d-0a27-4763-b7cb-100d4d5ab238
		  collapsed:: true
			- #laundry
			  idr:: 20000
			- бананы и джаму #shopping #banana #jamu
			  idr:: 35000
			- 11 хризантем и доставка #flowers
			  idr:: 49500
			- wrap, nutella crepe #food #delivery
			  idr:: 125000
			- #taxi #Tuta-House
			  idr:: 14000
			- пицца #delivery #pizza
			  idr:: 327000
			- #taxi #Adi-House-Moding
			  idr:: 10500
		- [[2025-05-31]]
		  id:: 3721467b-09c3-4fa2-921c-ff1f477ba65a
		  collapsed:: true
			- #app #english AI приложение по английскому 756.000 IDR
			  idr:: 756000
			- #rent #house
			  idr:: 5500000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #taxi #Tuta-House
			  idr:: 11500
			- #shop 2 молока и печенье
			  idr:: 47000
			- #taxi #Kirtan-House
			  idr:: 14000
			- #donation
			  idr:: 50000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #[[Alpha GPC]] #shopping
			  idr:: 595400
			- #shopping чехол лабиринт для телефона
			  idr:: 205100
	- ### June
	  collapsed:: true
		- Месяц June 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Jun 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-06-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-06-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-06-01]]
		  id:: cdc943d1-438b-466c-84de-1790424ba130
		  collapsed:: true
			- #delivery #вода Чай и воду 15 л
			  idr:: 133000
			- #taxi #Tuta-House
			  idr:: 11500
			- #taxi #Adi-House-Moding
			  idr:: 16500
		- [[2025-06-02]]
		  id:: 87009976-b83e-4ce4-90b7-25b87e12ce6e
		  collapsed:: true
			- Справка о проживании
			  idr:: 200000
			- Фото-студия - печать и сканирование документов
			  idr:: 6000
			- #shop Магазин - молоко, бананы, сливки
			  idr:: 90000
			- #food #delivery паста и оладьи
			  idr:: 106750
			- #taxi #Tuta-House
			  idr:: 11500
			- #taxi #Adi-House-Moding
			  idr:: 15500
			- #shop #Cocoku печенье
			  idr:: 90000
			- #kitas обновление адреса в КИТАС
			  idr:: 1500000
			- Transfers
			- Wise to Permata 1.000.000
			- Wise to Permata 1.500.000
		- [[2025-06-03]]
		  id:: 383120ce-d354-45bf-98f7-d180fd9fdc83
		  collapsed:: true
			- #vitamin Максиму за Ежовик
			  idr:: 600000
			- #food #delivery паста и оладьи
			  idr:: 106750
			- Transfers
			- Wise to Permata 2.000.000 IDR #Wise #Permata
			- Bybit 11.000 rub to 138.45 USDT #ByBit
		- [[2025-06-04]]
		  id:: d30c55bf-aa0e-482c-9830-82943e3ce659
		  collapsed:: true
			- #taxi на чаши к [[Артем]]
			  idr:: 23500
			- #shopping #Club-Sehat
			  idr:: 485000
			- #taxi #Adi-House-Moding
			  idr:: 11500
		- [[2025-06-05]]
		  id:: 92262580-ee0b-41b4-ac40-7a108a12a1a2
		  collapsed:: true
			- #вода
			  idr:: 26000
			- #flowers #delivery
			  idr:: 43500
			- #taxi #Tuta-House
			  idr:: 14000
			- #taxi #Cocoku #Adi-House-Moding такси в [[Adi House Moding]] через [[Cocoku]]
			  idr:: 17000
			- #shopping #Cocoku печенье и бананы
			  idr :: 102075
			- #godaddy makeb.net
			  idr:: 329224
			- #claude 1 month
			  idr:: 336112
		- [[2025-06-06]]
		  id:: 9b0a8fee-239a-4902-8f45-55e14909f384
		  collapsed:: true
			- #shopping #milk
			  idr:: 60000
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 15000
			- #grab #subscription
			  idr:: 24000
		- [[2025-06-07]]
		  id:: bf55e029-e8d5-4311-934e-f2f6bd94502d
		  collapsed:: true
			- #taxi #Tuta-House
			  idr:: 14000
			- #taxi #Kirtan-House
			  idr:: 16000
			- #taxi #Cocoku #Adi-House-Moding
			  idr:: 16000
			- #Cocoku #shopping
			  idr:: 84000
		- [[2025-06-08]]
		  id:: 91abae62-0620-4835-8d25-8af041484c2c
		  collapsed:: true
			- #taxi #shopping в СПА Four Seasons
			  idr:: 23500
			- #taxi #Adi-House-Moding
			  idr:: 46500
			- #shopping #Bintang
			  idr:: 275500
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-06-09]]
		  id:: a86f1e4c-3d21-4e6b-a2c4-17374e8c1d4f
		  collapsed:: true
			- #shopping 3 #milk
			  idr:: 60000
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #Cocoku #Adi-House-Moding
			  idr:: 16000
			- #shopping #Cocoku
			  idr:: 63000
		- [[2025-06-10]]
		  id:: 009e8eb2-8be3-4091-b259-82d167f3e5e1
		  collapsed:: true
			- #food #delivery Пицца с грибами
			  idr:: 94750
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 16000
		- [[2025-06-12]]
		  id:: db9772e2-c1e6-4176-94c7-6246eb1be732
		  collapsed:: true
			- #delivery #вода
			  idr:: 30000
			- #taxi #barbershop
			  idr:: 14000
			- #barbershop
			  idr:: 230000
			- #flowers
			  idr:: 28000
			- #taxi #Tea-House #Cocoku #Adi-House-Moding
			  idr:: 17000
			- #cow Махешик за июнь 5500 RUB
			- #delivery #pizza Белла Пицца - маленькая 4 сыра
			  idr:: 88700
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-06-13]]
		  id:: 57d39cee-9e9e-4b3f-980f-efb29deec9ef
		  collapsed:: true
			- #delivery #food Кукурузный суп и Чизкейк
			  idr:: 183350
			- #shopping #milk
			  idr:: 60000
			- #taxi #Tuta-House
			  idr:: 14000
			- #shopee #sox Заказал носки с доставкой
			  idr:: 29648
			- #mobile
			  idr:: 53000
			- #delivery #food #Tuta-House
			  idr:: 60000
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-06-14]]
		  id:: 030a091b-f473-4139-9305-46bd2ee22326
		  collapsed:: true
			- #taxi #Tea-House with tips
			  idr:: 19000
			- #taxi #Kirtan-House
			  idr:: 13000
			- #donation
			  idr:: 100000
			- #taxi #Cocoku #Adi-House-Moding
			  idr:: 17000
			- #shopping #Cocoku 4 печенье
			  idr:: 102000
		- [[2025-06-15]]
		  id:: 002afcd9-a501-4b77-8292-af36ffbc908a
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 14000
			- #taxi #Club-Sehat
			  idr:: 20500
			- #shopping #Club-Sehat гречка, сливки, кешью, печенье
			  idr:: 743500
			- #spa #coconut-spa Балийский массаж 90 минут
			  idr:: 200000
			- #taxi #Giordano #Adi-House-Moding
			  idr:: 20500
			- #shopping #Giordano носки, брюки, рубашка
			  idr:: 1491000
		- [[2025-06-16]]
		  id:: 98dca672-4e40-4dae-b828-32c5b9f7d80f
		  collapsed:: true
			- #taxi #flower-shop #Cocoku #Tuta-House
			  idr:: 18000
			- #flowers 9 белых роз по 3000 и оформление букета
			  idr:: 44000
			- #shopping #Cocoku фрукты
			  idr:: 85290
			- #delivery #food пицца из Белла
			  idr:: 118950
			- #taxi #Adi-House-Moding
			  idr:: 12000
		- [[2025-06-17]]
		  id:: 8f8a6701-3b80-45b6-bc22-3c47cc2bb814
		  collapsed:: true
			- #shopping Бананы, печенье, соль
			  idr:: 28000
			- #laundry
			  idr:: 40000
			- #shopee #clothes 2 рубашки
			  idr:: 240000
			- #shopee #clothes кремовые шраны
			  idr:: 111875
			- #Tokopedia #candle 10 деревянных фитилей
			  idr:: 38300
		- [[2025-06-18]]
		  id:: 64b06579-39d4-4160-b757-d455c6a2fe03
		  collapsed:: true
			- #shopping #milk
			  idr:: 60000
			- #taxi #Tea-House
			  idr:: 14000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #taxi #Pyramids-of-Chi
			  idr:: 14000
			- #food #Pyramids-of-Chi
			  idr:: 225000
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #donation Tailor App
			  idr:: 50000
		- [[2025-06-19]]
		  id:: 7754887b-4570-4f56-b2e2-1406231e82b7
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 16000
		- [[2025-06-20]]
		  id:: 5ece45f7-993e-495a-9359-aa123fc89698
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #Bintang
			  idr:: 16000
			- #Bintang удлинитель, бананы, масло, печенье
			  idr:: 283664
			- #spa #coconut-spa Балийский Массаж 90м
			  idr:: 200000
			- #print Распечатка и ламинирование Китаса
			  idr:: 7000
			- #taxi #cafe Raw Cocao
			  idr:: 16000
			- #cafe waffles and cocao
			  idr:: 126500
			- #cafe chocolate
			  idr:: 82250
			- #taxi #Adi-House-Moding #Tuta-House
			  idr:: 19000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #shopee Белые штаны
			  idr:: 112880
		- [[2025-06-21]]
		  id:: 266a9fc2-3536-4cfa-8ab4-85bccda79c1a
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 14000
			- #taxi #Adi-House-Moding #shop
			  idr:: 23000
			- #shopping Молоко и шоколадка
			  idr:: 34000
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Kirtan-House
			  idr:: 14000
			- #donation за Киртан
			  idr:: 100000
			- #taxi #Adi-House-Moding
			  idr:: 17000
			- #shopee
			  idr:: 90000
		- [[2025-06-22]]
		  id:: 27e9ba7e-ef77-4e49-9add-88524f809af8
		  collapsed:: true
			- #вода
			  idr:: 26000
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #shopping #shopee 3 накидки
			  idr:: 361663
		- [[2025-06-23]]
		  id:: 74d0153c-46dd-46aa-a55c-1b093a17b34b
		  collapsed:: true
			- #delivery Ginger Shot
			  idr:: 27000
			- #delivery Papaya leaf
			  idr:: 32000
			- #laundry
			  idr:: 24000
			- #taxi #Tea-House
			  idr:: 13000
			- #food #Healing-Center
			  idr:: 161000
			- #shopee Пакеты для чая
			  idr:: 71234
			- #food Шоколадка
			  idr:: 46000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #shopee Белые штаны
			  idr:: 92000
		- [[2025-06-24]]
		  id:: 6b088119-37f4-4c65-acd2-43e86cc14833
		  collapsed:: true
			- #taxi #VeraHouse
			  idr:: 29000
			- #taxi #Tea-House
			  idr:: 29000
			- #delivery #food Пица Белла и фри
			  idr:: 100823
			- #delivery 2 кокоса
			  idr:: 40000
			- #taxi #Cocoku #Adi-House-Moding
			  idr:: 16000
			- #shopping #Cocoku 6г ромашка, 3 пачки печенья
			  idr:: 87000
			- #food #delivery Вафли
			  idr:: 83485
			- #shopping #delivery 3 молока
			  idr:: 66900
		- [[2025-06-25]]
		  id:: 7642ce14-550f-4438-80e5-6f2b896d7b02
		  collapsed:: true
			- #delivery Ginger Guice
			  idr:: 84000
			- #taxi #Tea-House
			  idr:: 20000
			- #taxi #Adi-House-Moding #Cocoku
			- idr: 15000
			- #shopping #Cocoku
			  idr:: 143675
		- [[2025-06-26]]
		  id:: 2ffeebf1-7744-4219-9b5e-5b78c278fd2a
		  collapsed:: true
			- #telkomsel
			  idr:: 5600
			- #food #delivery Вафли
			  idr:: 78865
			- #food #delivery картошка фри
			  idr:: 42375
			- #clothes #shopee Ремень
			  idr:: 83700
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-06-27]]
		  id:: b4554c33-8e45-4305-b49b-acb4289804ef
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #coconut-spa
			  idr:: 13000
			- #spa Массаж со скрабом из соли
			  idr:: 250000
			- #taxi #Adi-House-Moding
			  idr:: 24500
			- #shopping #Satvika-Bhoga
			  idr:: 745000
			- #flowers 9 цветов по 3
			  idr:: 27000
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Wayan-House
			  idr:: 14000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #subscription Scispace
			  usd:: 84
		- [[2025-06-28]]
		  id:: 4d278a75-5cb3-4617-beb0-a3591426dc34
		  collapsed:: true
			- #taxi #atm
			  idr:: 15000
			- #taxi #Tea-House
			  idr:: 20000
			- #subscription #Apple-Drive
			  idr:: 15000
			- #remedy #Planets Граха Шанти
			  idr:: 8000000
			- #remedy #Planets Граха Шанти
			  idr:: 3040000
			- #taxkz Налог на имущество
			  kzt:: 871
			- #delivery #food шоколадный торт и белые суши
			  idr:: 182250
			- #delivery Органик сахар
			  idr:: 37000
			- #Tokopedia Now Alpha GPC
			  idr :: 630900
		- [[2025-06-29]]
		  id:: 06dd4801-86b8-4d33-8014-1fea4f22a3f2
		  collapsed:: true
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-06-30]]
		  id:: 85ef9420-0f40-4b92-a0b1-77bb86eec8d8
		  collapsed:: true
			- #shopping Бананы
			  idr:: 10000
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #delivery
			  idr:: 94900
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 15000
	- ### July
	  collapsed:: true
		- Месяц July 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Jul 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-07-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-07-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-07-01]]
		  id:: b15093dd-a3b5-4caa-86c8-9ba480740887
		  collapsed:: true
			- #taxi к Роме
			  idr:: 29000
		- [[2025-07-02]]
		  id:: 0b09a250-8e21-484f-893b-7ca7f063597b
		  collapsed:: true
			- #вода
			  idr:: 26000
			- #shopping 3 банана и зубная паста
			  idr:: 16000
			- #shopping 3 молока, 4 батарейки и 1 кола
			  idr:: 99000
			- #taxi #Cocoku #Tuta-House
			  idr:: 16000
			- #shopping #Cocoku 6 Печенье
			  idr:: 126000
			- #taxi #shopping #Adi-House-Moding
			  idr:: 16000
			- #shopping сникерс и 6 сливок
			  idr:: 49000
			- #food #delivery Пицца
			  idr:: 46350
			- #delivery Ginger juice
			  idr:: 92000
			- #taxi #Tuta-House
			  idr:: 21000
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-07-03]]
		  id:: edc5400f-a48c-47d2-b0af-3eeee4e8f8b9
		  collapsed:: true
			- #house Оплата за дом
			  idr:: 5500000
			- #shopee Фетили
			  idr:: 9600
			- #taxi #United-Healing-Center
			  idr:: 19000
			- #taxi #print-shop
			  idr:: 18500
			- #print-shop Печать и скан
			  idr:: 8000
			- #delivery #food Маргарита
			  idr:: 51350
			- #taxi #Adi-House-Moding
			  idr:: 20000
		- [[2025-07-04]]
		  id:: 2599b8bd-3bcb-49bd-80b8-180795b547e8
		  collapsed:: true
			- #taxi #Cocoku #Tuta-House
			  idr:: 16000
			- #shopping #Cocoku Печенья
			  idr:: 105000
			- #laundry
			  idr:: 15000
			- #shopping Дождевик
			  idr:: 20000
			- #taxi #Adi-House-Moding
			  idr:: 24000
			- #direct Амелия и Тамара
			  rub:: 4800
			- #donation #cow Махешику
			  rub:: 5500
		- [[2025-07-05]]
		  id:: 8ff33496-5b8a-409d-a0a3-00b84801bfe7
		  collapsed:: true
			- #taxi #Cocoku #Tuta-House
			  idr:: 16000
			- #delivery Ginger Juice
			  idr:: 86000
			- #taxi #Adi-House-Moding
			  idr:: 16000
			- #shopping 4 банана
			  idr:: 10000
			- #taxi #Sayuri на Киртан и Сатсанг
			  idr:: 15000
			- #food #Sayuri Тортики
			  idr:: 116500
			- #taxi #Tuta-House на Арати
			  idr:: 24000
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-07-06]]
		  id:: 455b8efa-e109-4961-a12c-2a15111c0241
		  collapsed:: true
			- #subscription #ChatGPT
			  idr:: 334423
			- #taxi #Tuta-House #Cocoku
			  idr:: 16000
			- #laundry Штаны, Полотенце
			  idr:: 15000
			- #taxi #Adi-House-Moding на машине (в дождь)
			  idr:: 46000
			- #shopping #jamu #Pengkolan
			  idr:: 27000
			- перевод менеджеру
			  RUB:: 10000
		- [[2025-07-07]]
		  id:: e9fcf316-abd5-40ad-9f85-cc50c663b1ba
		  collapsed:: true
			- #food #delivery Raw Ginger Juice
			  idr:: 92000
			- #food #delivery Блины с эклером
			  idr:: 174000
			- #taxi #Tea-House
			  idr:: 10000
			- #taxi #Adi-House-Moding #shop с чаевыми
			  idr:: 19000
			- #shopping 3 молока, 2 кокосовые сливки, 1 сникерс
			  idr:: 86000
			- #вода
			  idr:: 26000
			- #delivery #food Вафли и конфеты
			  idr:: 184600
		- [[2025-07-08]]
		  id:: 9e926c02-ba79-4a8b-9f8c-af51de38d3af
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 10000
			- #taxi #Adi-House-Moding #Cocoku
			  idr:: 16000
			- #shopping #Cocoku 4 Печенья, Чипсы и Джаму
			  idr:: 158000
			- #delivery #food Медовик
			  idr:: 89000
		- [[2025-07-09]]
		  id:: e36e8450-350e-4146-bfbc-307774272318
		  collapsed:: true
			- Оле ЗП
			  rub:: 19880
			- #taxi #Tea-House
			  idr:: 10000
			- #taxi #Svarga-Loka
			  idr:: 14000
			- #therapy Танцевальная Терапия
			  idr:: 350000
			- #taxi #Bintang
			  idr:: 13000
			- #shopping #Bintang Масло, Бананы, Кешью, Чай, Печенье
			  idr:: 364499
			- #spa #coconut-spa
			  idr:: 250000
			- #taxi #Adi-House-Moding #flower-shop
			  idr:: 18500
			- #flowers 9 цветов по 3
			  idr:: 27000
		- [[2025-07-10]]
		  id:: 37f007c2-c346-4f34-96d5-e3b4c71d3d9a
		  collapsed:: true
			- #CRM Менеджер
			  rub:: 10720
			- #taxi #Cocoku #Sasuka-Villa-Ubud
			  idr:: 16000
			- #donation Благодарность за организацию
			  idr:: 100000
			- #taxi #Adi-House-Moding #Tea-House
			  idr:: 16000
			- #Mobile-Internet
			  idr:: 29000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #food #delivery Жареная кукуруза, суши и торт
			  idr:: 145525
			- #taxi #Tuta-House
			  idr:: 19000
			- #taxi #Adi-House-Moding
			  idr:: 14000
		- [[2025-07-11]]
		  id:: d76e65ae-112f-43b1-ac47-c0560316d808
		  collapsed:: true
			- #taxi Нотариус
			  idr:: 25000
			- #taxi #Tea-House
			  idr:: 28000
			- #taxi #Adi-House-Moding
			  idr:: 14000
		- [[2025-07-12]]
		  id:: 70bcc31f-2723-4825-9cea-dacad6d7a9a5
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 15000
			- #taxi #Adi-House-Moding #Cococu-Laundry #shop
			  idr:: 17000
			- #laundry
			  idr:: 21000
			- #shopping 5 Кокосовые сливки, 3 Молоко, 1 мороженое
			  idr:: 107000
			- #food #delivery Бургер и тортик из Plant Bistro
			  idr:: 161410
			- #taxi #Kirtan-House
			  idr:: 13000
			- #donation за Киртан и просад
			  idr:: 100000
			- #taxi #Adi-House-Moding
			  idr:: 12000
			- #subscription #[[2020-07-08 DeployHQ Subscription]]
			  idr:: 181969
		- [[2025-07-13]]
		  id:: 571a4f18-5517-4935-a315-da99b45a37d5
		  collapsed:: true
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding #Cocoku
			  idr:: 21000
			- #shopping 6 печенье
			  idr:: 126000
			- #shopping 4 банана
			  idr:: 8000
		- [[2025-07-14]]
		  id:: b0490328-5232-417c-ab04-7a60445076d7
		  collapsed:: true
			- #shopping Jami
			  idr:: 10000
			- #taxi #Cococu-Laundry #Tea-House
			  idr:: 16000
			- #shopping #United-Healing-Center
			  idr:: 46000
			- #food #Pengkolan Кари, Оладьи, Ананасовый сок
			  idr:: 117652
			- #taxi #Adi-House-Moding
			  idr:: 17000
		- [[2025-07-15]]
		  id:: 46d2028b-1e2c-4c94-b30e-d2c05286d1e6
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #Bintang
			  idr:: 13000
			- #shopping #Bintang Печенье, Хлеб, Овсянка, Майка
			  idr :: 280070
			- #food #buffet
			  idr:: 61800
			- #shopping #Club-Sehat Сыр, Греча, Кешью
			  idr:: 221000
			- #spa  Hot stone massage
			  idr:: 300000
			- #taxi #Satvika-Bhoga #Manis-Flower #Adi-House-Moding
			  idr:: 26000
			- #shopping #Satvika-Bhoga Кокао, Шоколадка
			  idr:: 195000
			- #flowers 5
			  idr:: 16000
			- #laundry в [[Cocoku]]
			  idr:: 22500
			- #taxi #Tuta-House
			  idr:: 14000
			- #taxi #Adi-House-Moding
			  idr:: 12000
		- [[2025-07-16]]
		  id:: 001163f4-535b-472d-9cef-2105749e8f2f
		  collapsed:: true
			- #вода
			  idr:: 26000
			- #taxi #barbershop
			  idr:: 13000
			- #barbershop
			  idr:: 130000
			- #taxi #Tea-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #taxi #Tuta-House
			  idr:: 17000
			- #taxi #Adi-House-Moding
			  idr:: 12000
		- [[2025-07-17]]
		  id:: 5aff25eb-f986-4e6b-a1ad-335da236e522
		  collapsed:: true
			- #taxi #shop #Cococu-Laundry #Tea-House
			  idr:: 17000
			- #shopping бананы, молоко
			  idr:: 30000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #subscription [[Прем Баба]] академия
			  idr:: 621009
			- #CRM Менеджеру
			  rub:: 10000
		- [[2025-07-18]]
		  id:: 596b7a85-66c4-4f6c-b7d2-93996ccc15ae
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 6500
			- #taxi #Dikha-Print
			  idr:: 13000
			- #printing
			  idr:: 5000
			- #shopping #Green-Habbit
			  idr:: 241000
			- #taxi #Adi-House-Moding
			  idr:: 11000
			- #food #delivery 4 сыра из Ла Бараки и чаевые 10000
			  idr:: 140280
			- #taxi #Tuta-House
			  idr:: 13000
			- #taxi #Adi-House-Moding
			  idr:: 12000
		- [[2025-07-19]]
		  id:: 9833ce2e-f3f2-4a77-b451-58e2f62693a7
		  collapsed:: true
			- #etke  Matrix Element
			  idr:: 600000
			- #taxi #Tuta-House
			  idr:: 6500
			- #taxi #Cocoku #Adi-House-Moding
			  idr:: 15000
			- #laundry
			  idr:: 25500
			- #shopping #Cocoku 5 печенье
			  idr:: 105000
		- [[2025-07-20]]
		  id:: 6f80fc34-474c-4d3a-a14f-18b026156d6a
		  collapsed:: true
			- #taxi #Tuta-House
			  idr:: 6500
			- #taxi #Adi-House-Moding
			  idr:: 12000
		- [[2025-07-21]]
		  id:: b90dd071-f802-43fe-8558-87f6d0e8e423
		  collapsed:: true
			- #delivery #flowers 9 по 3000 плюс доставка за 15000
			  idr:: 42000
			- #taxi #Tuta-House
			  idr:: 10000
			- #taxi #Adi-House-Moding
			  idr:: 12000
			- Подписка на Transkriptor
			  usd:: 19.00
		- [[2025-07-22]]
		  id:: 86b752b0-2747-428c-a2b7-74617095aabe
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 19000
			- #shopping 3 молока, белый шоколад, 2 банана, 5 сливки
			  idr:: 148000
			- #taxi #shop #Adi-House-Moding
			  idr:: 15000
		- [[2025-07-23]]
		  id:: 304465d0-babe-4c60-9dc2-75a000beca50
		  collapsed:: true
			- #subscription #mobile-Internet
			  idr:: 31000
			- #taxi #Tea-House
			  idr:: 13000
			- #delivery #food Pyramids of Chi суши, оладьи, торт, сок
			  idr:: 305500
			- #taxi #Cocoku #Adi-House-Moding
			  idr:: 16000
			- #shopping #Cocoku
			  idr:: 84000
		- [[2025-07-24]]
		  id:: e78689a8-b771-45a1-b267-0871e3020b4e
		  collapsed:: true
			- #subscription Claude.ai
			  idr:: 335866
			- #taxi #Tuta-House
			  idr:: 14000
			- #food #delivery 2 Пиццы из Белла Пицца и tips 5000
			  idr:: 236465
			- #taxi #Adi-House-Moding
			  idr:: 13000
		- [[2025-07-25]]
		  id:: f9cc4388-59ab-473e-8ff7-e60c06fefdce
		  collapsed:: true
			- #taxi #Tea-House
			  idr:: 14000
			- #taxi #Piramids-Of-Chi
			  idr:: 15000
			- #food #Piramids-Of-Chi
			  idr:: 335000
			- #taxi #Tuta-House
			  idr:: 15000
			- #delivery Fresh Ginger Juice
			  idr:: 93000
			- #taxi #Adi-House-Moding
			  idr:: 14000
		- [[2025-07-26]]
		  id:: 011c9ff3-39b9-4ca7-9fc9-d2b12359892d
		  collapsed:: true
			- #taxi #shop
			  idr:: 21500
			- #taxi #Sacred-Cocao
			  idr:: 14000
			- #food #Sacred-Cocao
			  idr:: 137500
			- #taxi #Bintang
			  idr:: 0
			- #shopping #Bintang
			  idr:: 202934
			- #coconut-spa
			  idr:: 300000
			- #food #buffet
			  idr:: 63000
			- #taxi #Adi-House-Moding
			  idr:: 15500
			- #taxi #Cococu #Tea-House Через стирку
			  idr:: 17000
			- #Cococu Хлеб Sour Dough
			  idr:: 75000
			- #taxi #Adi-House-Moding
			  idr:: 15000
			- #CRM менеджеру
			  rub:: 11520
		- [[2025-07-27]]
		  id:: c8bbb7fd-54d3-4d8d-8980-34ab29968b39
		  collapsed:: true
			- #taxi #Tea-House #Cocoku #United-Healing-Center
			  idr:: 19000
			- #Cococu-Laundry
			  idr:: 30000
			- #food #United-Healing-Center
			  idr:: 115000
			- #taxi #Adi-House-Moding
			  idr:: 16000
			- #CRM [[Оля]]
			  rub:: 13160
		- [[2025-07-28]]
		  id:: ea4f368c-6046-47b7-bd17-7534cf9ad919
		  collapsed:: true
			- #shopping 3 молока, кола, печенье
			  idr:: 89000
			- #taxi #Budda-Yana к Лене
			  idr:: 25500
			- #taxi #Adi-House-Moding
			  idr:: 23500
		- [[2025-07-29]]
		  id:: 366fd7d4-419f-4bcf-a606-ed2d0ab749c2
		  collapsed:: true
			- #taxi #Bintang
			  idr:: 20500
			- #Bintang бананы, чай, хлеб, батарейки
			  idr:: 139654
			- #Club-Sehat кешью, сыр
			  idr:: 0
			- #taxi #Manis-Flower #Serenity-SPA
			  idr:: 19000
			- #Serenity-SPA Hot Stone Massage #cash
			  idr:: 250000
			- #taxi #Cococu-Laundry #Adi-House-Moding #Usada
			  idr:: 37000
			- #laundry
			  idr:: 19500
			- #food #Usada
			  idr:: 204430
			- #taxi #Adi-House-Moding
			  idr:: 17000
		- [[2025-07-30]]
		  id:: 3d5242ab-8af4-4b27-b068-a0881b6c0c3f
		  collapsed:: true
			- #CRM менеджеру
			  rub:: 11400
			- #taxi #Tuta-House
			  idr:: 25000
			- #taxi #Adi-House-Moding
			  idr:: 21000
		- [[2025-07-31]]
		  id:: 7e90f360-1964-4fd0-867c-a32b37d0d06f
		  collapsed:: true
			- #вода
			  idr:: 26000
			- #food #delivery Пицца и сок
			  idr:: 98700
			- #rent #house Оплата за дом
			  idr:: 5500000
	- ### August
	  collapsed:: true
		- Месяц August 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Aug 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-08-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-08-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-08-01]]
		  id:: 1096a350-83fe-43cf-9218-2b5f18dee883
		  collapsed:: true
			- #taxi #coconut-spa
			  idr:: 17000
			- #coconut-spa Hot Stone Massage 90 min
			  idr:: 300000
			- #taxi #Satvika-Bhoga #Manis-Flower #Sayuri
			  idr:: 16500
			- #shopping #Satvika-Bhoga Кускус и шоколад
			  idr::  158000
			- #shopping #flowers
			  idr:: 27000
			- #Sayuri  тудэй спешил, мате, тосты, благовония, сок с собой
			  idr:: 413500
			- #taxi #Adi-House-Moding
			  idr:: 20500
			- #shopping 3 чокопай, 2 молоко
			  idr:: 50000
			- #CRM Оплата [[Оля]]
			  rub:: 14080
			- #CRM Оплата Менеджеру
			  rub:: 10920
		- [[2025-08-02]]
		  id:: 677e9f35-07d8-4481-b6c1-b2b393b4f568
		  collapsed:: true
			- #BCA Обслуживание карты
			  idr:: 15243
			- #taxi #Pyramids-of-Chi
			  idr:: 11000
			- #food #Pyramids-of-Chi Сок и lemon tart
			  idr:: 138000
			- #shopping Благовония Lemon Grass
			  idr:: 40000
			- #taxi #Tea-House на встречу с Ториком и Мини
			  idr:: 14000
			- #taxi #Tuta-House
			  idr:: 11000
			- #taxi #Adi-House-Moding
			  idr:: 14000
		- [[2025-08-03]]
		  id:: d9a07bc1-ecea-4191-b43a-b4591083c645
		  collapsed:: true
			- #CRM [[Оля]] с ВТБ
			  rub:: 12460
			- #shopping 4 банана и соль
			  idr:: 10000
			- #taxi #Tea-House
			  idr:: 15000
			- #taxi #Pyramids-of-Chi Карри и торт
			  idr:: 14000
			- #food #Pyramids-of-Chi
			  idr:: 156000
			- #Mobile-Internet
			  idr:: 51500
		- [[2025-08-04]]
		  id:: e22ddd90-58ba-417d-a941-fe4498f4d524
		  collapsed:: true
			- #taxi #Cococu-Laundry #shopping #Tea-House с чаевыми за помощь
			  idr:: 44000
			- #food #United-Healing-Center Вроп, брауни и матча
			  idr:: 184000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #donation #cow Махешику
			  rub:: 5500
		- [[2025-08-05]]
		  id:: 028bdb55-ee2c-4d27-b90b-d34deadb7131
		  collapsed:: true
			- #taxi на Киртан
			  idr:: 9000
			- #taxi #Cococu-Laundry #Adi-House-Moding
			  idr:: 17000
			- #laundry
			  idr:: 24000
			- #shopping Джаму
			  idr:: 10000
		- [[2025-08-06]]
		  id:: 64884be7-41de-4d4b-a166-272aaa3f46c9
		  collapsed:: true
			- #donation  Music Art Yoga Fest
			  idr:: 500000
			- #delivery #food из Bella Pizza - Пицца, сок и фри
			  idr:: 155830
			- #taxi на фестиваль
			  idr:: 24500
			- #taxi в [[Adi House Moding]] через [[Cocoku]]
			  idr:: 30000
			- #shopping #Cococu
			  idr:: 167000
			- #subscription 1 месяц CapCut
			  idr:: 15000
		- [[2025-08-07]]
		  id:: 11961a89-11da-4ff2-941c-5af07144a829
		  collapsed:: true
			- #taxi #Bintang
			  idr:: 12000
			- #shopping #Bintang Хлеб, масло, печенье
			  idr:: 137000
			- #shopping #Club-Sehat Сливки, греча, кешью, 2 сыра
			  idr:: 495000
			- #food Буфет
			  idr:: 61500
			- #coconut-spa Hot Stone Massage 90min
			  idr:: 300000
			- #taxi #Manis-Flower #Adi-House-Moding
			  idr:: 25500
			- #shopping #Manis-Flower 10 стеблей по 4000
			  idr:: 41200
			- #delivery #food Доставка Вафли
			  idr:: 85300
		- [[2025-08-08]]
		  id:: 28b22c45-dfa2-48fe-be0e-bb2f74b44168
		  collapsed:: true
			- #service Справка из полиции
			  idr:: 2000000
			- #вода
			  idr:: 25000
			- #taxi #Tea-House #Cococu-Laundry
			  idr:: 17000
			- #taxi #Adi-House-Moding
			  idr:: 16000
			- #taxi на концерт
			  idr:: 20500
			- #donation концерт
			  idr:: 450000
			- #donation за мурти Лакшми
			  idr:: 100000
			- #taxi #Adi-House-Moding
			  idr:: 17000
			- #CRM менеджеру
			  rub:: 11280
			- #subscription Кибер-Прайм на 1 месяц
			  rub:: 3590
		- [[2025-08-09]]
		  id:: 8881bc74-2aee-4067-bdea-621c0636789e
		  collapsed:: true
			- #delivery #shopping Чемодан с доставкой
			  idr:: 840000
			- #taxi #Tea-House
			  idr:: 14000
			- #taxi #Cococu-Laundry #Adi-House-Moding с чаевыми 6000
			  idr:: 23000
			- #laundry
			  idr:: 15000
			- #shopping рядом со стиркой - Лимонад и Витамин Ц
			  idr:: 10000
			- #shopping дальний магазин - 3 молоко, шоколад
			  idr:: 93000
			- #subscription Telegram Premuim за год
			  idr:: 450000
			- #taxi на концерт
			  idr:: 27000
			- #taxi #Adi-House-Moding
			  idr:: 28000
		- [[2025-08-10]]
		  id:: 94b44a81-3969-4c2a-9c87-1d2782f172c2
		  collapsed:: true
			- #shopping Лепестки и вода
			  idr:: 14000
			- #taxi на Сатсанг
			  idr:: 321500
			- #shopping K Mart по поути на Сатсанг - шоколадка
			  idr:: 27000
			- #taxi #Adi-House-Moding
			  idr:: 41500
		- [[2025-08-11]]
		  id:: 9ab27e6c-f05b-44a5-bee6-922c612d98e0
		  collapsed:: true
			- #food #delivery #Fortunate-Coffee - Кукуруза, суши, пирожки, печенье 250750
			  idr:: 250750
			- #Mobile-Internet 32GB
			  idr:: 70000
			- #subscription #Manus-AI
			  idr:: 249000
			- #taxi #Tuta-House
			  idr:: 17000
			- #taxi #Adi-House-Moding
			  idr:: 13000
			- #CRM #Manager-Salary
			  rub:: 11040
		- [[2025-08-12]]
		  id:: fb722c89-c664-496e-b231-18941006a0ab
		  collapsed:: true
			- #delivery #food #Pengkolan Блины, оладьи, яблочный торт и ласси
			  idr:: 188500
			- #вода для #Tuta-House
			  idr:: 26000
			- #taxi #Tuta-House
			  idr:: 11500
			- #delivery #Plant-Bistro 2 порции суши
			  idr:: 213200
			- #taxi #Adi-House-Moding
			  idr:: 14000
		- [[2025-08-13]]
		  id:: e0bc0d13-ec9b-4a64-9d7c-b88ca170bd5f
		  collapsed:: true
			- #taxi в Банк
			  idr:: 16000
			- #food #Sayuri
			  idr:: 342500
			- #taxi на Бади Перкашн
			  idr:: 16000
			- #donation Бади Перкашн
			  idr:: 100000
			- #taxi #Adi-House-Moding через #Cococu
			  idr:: 29000
			- #food #Cocou Бананы, печенье и сок
			  idr:: 142150
			- #delivery  Pure Grape Juice 300ml
			  idr:: 72000
		- [[2025-08-14]]
		  id:: bf0731e7-116a-4988-af8f-fb0c9ab8eec7
		  collapsed:: true
			- #taxi #coconut-spa
			  idr:: 17000
			- #coconut-spa Hot Stone Massage 90 min
			  idr:: 300000
			- #taxi #Satvika-Bhoga #Manis-Flower #Sayuri
			  idr:: 16500
			- #shopping #Satvika-Bhoga Кускус и шоколад
			  idr::  158000
			- #shopping #flowers
			  idr:: 27000
			- #Sayuri  тудэй спешил, мате, тосты, благовония, сок с собой
			  idr:: 413500
			- #taxi #Adi-House-Moding
			  idr:: 20500
			- #shopping 3 чокопай, 2 молоко
			  idr:: 50000
			- #CRM Оплата [[Оля]]
			  rub:: 14080
			- #CRM Оплата Менеджеру
			  rub:: 10920
		- [[2025-08-15]]
		  id:: 6ed0dd8e-9485-49a3-8193-da3d874e72c5
		  collapsed:: true
			- #taxi #Joyously-Raw занятие с Рассвет
			  idr:: 20500
			- #donation #Joyously-Raw заняте с Рассвет
			  idr:: 100000
			- #food #Joyously-Raw Авокадо тост, Матча латте с Алмонд милк
			  idr:: 115000
			- #food #Plant-Bistro пироженное и сок
			  idr:: 144000
			- #taxi #Tuta-House
			  idr:: 17000
			- #taxi #Adi-House-Moding
			  idr:: 14000
		- [[2025-08-16]]
		  id:: b7c4664e-2b6a-4b20-bdf6-03a9176765a4
		  collapsed:: true
			- #food #delivery Пицца из Bella
			  idr:: 141200
		- [[2025-08-17]]
		  id:: 5cfcb224-ffa6-4103-b227-3f26395e275c
		  collapsed:: true
			- #book Аудио книга - 2 жизни
			  idr:: 69000
			- #taxi #Tuta-House
			  idr:: 14000
			- #taxi #Sayuri
			  idr:: 16000
			- #donation Jeremy Kirtan
			  idr:: 250000
			- #donation Мурти Ганеша
			  idr:: 100000
			- #shopping шоколад
			  idr:: 77500
			- #taxi #Adi-House-Moding
			  idr:: 18000
		- [[2025-08-18]]
		  id:: 00aa720b-b4bf-4bf2-a554-a6a7085bef87
		  collapsed:: true
			- #taxi #Cococu-Laundry #shop #Adi-House-Moding
			  idr:: 18000
			- #shopping #Cococu 3 печенья, 4 банана
			  idr:: 79450
			- #shopping #Cococu Pineapple Mint Juice
			  idr:: 59000
			- #shopping 6 сливки 2 молоко
			  idr:: 108000
			- #taxi #Piramids-Of-Chi
			  idr:: 10000
			- #вода
			  idr:: 30000
			- #food #Piramids-Of-Chi Суши и eggplant vegan cheese rolls и цинамон кейк
			  idr:: 231000
			- #donation Light Sound Vibration
			  idr:: 850000
			- #CRM ЗП [[Оля]]
			  rub:: 12880
		- [[2025-08-19]]
		  id:: 4d81312d-1474-47c3-a69d-eb6e33b72f7a
		  collapsed:: true
			- #taxi #Joyously-Raw
			  idr:: 20500
			- #Manis-Flower #flowers цветы
			  idr:: 27000
			- #taxi #Adi-House-Moding
			  idr:: 15500
			- #taxi #dentist
			  idr:: 16000
			- #dentist Чистка зубов
			  idr:: 600000
			- #shopping Нитка для зубов, Толак Ангин, Нюхолка
			  idr:: 74650
			- #laundry
			  idr:: 22500
			- #CRM менеджеру
			  rub:: 11520
		- [[2025-08-20]]
		  id:: f2283736-d4ae-4b78-861b-68a1292b32b8
		  collapsed:: true
			- #taxi  стоматологу
			  idr:: 16000
			- #dentist #signature Пломбирование 2 зуба
			  idr:: 1200000
			- #taxi на Рентген зубов
			  idr:: 16000
			- #dentist #signature Рентген зубов
			  idr:: 400000
			- #taxi в Барбершоп
			  idr:: 30500
			- #barbershop
			  idr:: 130000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #food #delivery Пицца из Белла - 4 сыра
			  idr:: 83230
			- #taxi в Сарасвати Темпл
			  idr:: 26500
			- #donation Бади Перкашн Бади Перкашн
			  idr:: 100000
			- #taxi #Adi-House-Moding
			  idr:: 28000
			- #shopping Джаму
			  idr:: 10000
			- #shopping #Tokopedia AlphaGPC, Lion’s Mane
			  idr:: 1189000
		- [[2025-08-21]]
		  id:: 25cfff61-db1e-4a04-af49-8c862d3e46ec
		  collapsed:: true
			- #taxi Permata
			  idr:: 16000
			- #taxi #Adi-House-Moding
			  idr::19500
			- #donation Адити
			  idr:: 40000
			- #donation Адити
			  idr:: 48000
			- #taxi #dentist
			  idr:: 16000
			- #dentist #signature
			  idr:: 1150000
			- #shopping Аптека - нить для зубов
			  idr:: 26000
			- #taxi #Pyramids-of-Chi
			  idr:: 14000
			- #Pyramids-of-Chi #signature Ancient Sound Healing
			  idr:: 350000
			- #food #Pyramids-of-Chi #signature
			  idr:: 266000
			- #taxi #Tea-House - кари с нутом, суши и кэрот кейк
			  idr:: 20000
			- #food #signature Итальянское кафе - Равиоли и кокао
			  idr:: 169070
		- [[2025-08-22]]
		  id:: a3b49cc9-3cf1-41d9-aa85-1bb1194197d7
		  collapsed:: true
			- #taxi #dentist
			  idr:: 16000
			- #dentist #signature 2 зуба
			  idr:: 1150000
			- #dentist #signature Зубная нить
			  idr:: 100000
			- #taxi #Piramids-Of-Chi
			  idr:: 16500
			- #service #signature Scalar Healing Energy
			  idr:: 650000
			- #food #signature Gyoza and sushi
			  idr:: 174000
			- #shopping благовония
			  idr:: 40000
		- [[2025-08-23]]
		  id:: cc9e95a9-ff16-4dc8-b650-f06ded54c42e
		  collapsed:: true
			- #study Жанна Петухова - ИИ без воды - уроки с [[2025-08-28]]
			  rub:: 990
			- #food #delivery Манты с тыквой, шашлык из Грибов, винегрет, айран, Наан
			  idr:: 327000
			- #delivery Listerine
			  idr:: 17000
			- #delivery #flowers 11 белых с доставкой
			  idr:: 47500
			- #shopping Ежовик
			  idr:: 600000
			- #taxi к Максим
			  idr:: 15000
			- #ceremony у Максима
			  idr:: 1000000
			- #food #Cocoku 4 банана, фруктовая тарелка и ананасовый сок
			  idr:: 86000
		- [[2025-08-24]]
		  id:: a2900549-9f81-4567-9a2c-0dcf0bb4d6a5
		  collapsed:: true
			- #food #delivery
			  idr:: 155750
			- #taxi #Alchemy
			  idr:: 20500
			- #donation Каруника
			  idr:: 350000
			- #taxi #Adi-House-Moding
			  idr:: 18000
		- [[2025-08-25]]
		  id:: ddc4a35a-f87c-4994-9044-ca5db9adab90
		  collapsed:: true
			- #taxi авто такси в Дом Гуру и проезд по мосту
			  idr:: 368500
			- #laundry
			  idr:: 22000
			- #taxi авто такси в кафе Уша
			  idr:: 261000
			- #food #Usha-cafe вареники, квас, оливье
			  idr:: 167475
			- #taxi #Tuta-House
			  idr:: 21500
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #shopping Молоко и 4 батарейки
			  idr:: 32000
			- #shopping Джаму и 4 бананы
			  idr:: 20000
			- #CMR ЗП Оле
			  rub:: 13020
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #shopping Молоко и 4 батарейки
			  idr:: 32000
			- #shopping Джаму и 4 бананы
			  idr:: 20000
			- #ceremony Ягья Ганешу
			  rub:: 1300
			- #ceremony Питри Пакша
			  rub:: 5000
			- #food #delivey #Pengkolan Ужин - Wrap
			  idr:: 74000
		- [[2025-08-26]]
		  id:: 31a666c7-e3d2-474c-b8f5-24d86fc4041a
		  collapsed:: true
			- #taxi Ra-Family
			  idr:: 32500
			- #donation Круг Света
			  idr:: 100000
			- #taxi #Adi-House-Moding
			  idr:: 31000
			- #taxi #Cash TheChai
			  idr:: 35000
			- #shopping TheChai благовония Spices
			  idr:: 25000
			- #taxi #Adi-House-Moding
			  idr:: 28000
			- #food #delivery 2 Вафли, какао
			  idr:: 220900
		- [[2025-08-27]]
		  id:: d57a7d37-4dcf-4642-9e20-a1cdb88fe0a6
		  collapsed:: true
			- #delivery Доставка чаш с типс
			  idr:: 139000
			- #apps Autopad App
			  idr:: 99000
			- #shopping #Tokopedia Переходники
			  idr:: 196100
			- #laundry Стирка
			  idr:: 22500
			- #taxi #Alchemy
			  idr:: 35500
			- #service #Jeremy Kirtan for Ganesh
			  idr:: 450000
			- #food #Alchemy Салат с рисом и грибами
			  idr:: 115500
			- #taxi #Ubud-Shisha
			  idr:: 21000
			- #Ubud-Shisha Passion fruit и чай
			  idr:: 35000
			- #taxi #Adi-House-Moding
			  idr:: 19500
		- [[2025-08-28]]
		  id:: 2233c71c-2af8-47a0-aa15-2c210ede9975
		  collapsed:: true
			- #taxi #United-Healing-Center
			  idr:: 16000
			- #food #United-Healing-Center Butternut feta and cacao
			  idr:: 155250
			- #food шоколад
			  idr:: 103000
			- #taxi #Adi-House-Moding
			  idr:: 14000
			- #food #delivery Пицца Бурата без глютена
			  idr:: 202000
			- #food #delivery Оливье и квас из #Usha-cafe
			  idr:: 165000
			- #subscription e2language за 6 месяцев
			  idr:: 1424500
		- [[2025-08-29]]
		  id:: 4016454f-06e2-46ee-a451-2a311476834e
		  collapsed:: true
			- #taxi #Tuta-House
			  idr:: 15000
			- #food #Healing-Center Гранола и распечатка
			  idr:: 37500
			- #taxi #Adi-House-Moding
			  idr:: 17000
			- #taxi #Bali-Airport
			  idr:: 350000
			- #sim Amaysim
			  aud:: 12
			- #food #plane Peppermint Tea
			  aud:: 5
			- #food #plane quiche veggies
			  aud:: 12
		- [[2025-08-30]]
		  id:: 0b4abc84-d905-409a-b685-ce77a9eac0b7
		  collapsed:: true
			- #shopping #ALDI Timtam
			  aud:: 4.51
			- #shopping #Coles зубная паста и кокосовые сливки
			  aud:: 5.85
		- [[2025-08-31]]
		  id:: eb0af217-d2c4-49b9-baf3-eed5048aec3f
		  collapsed:: true
			- #shopping деревянная ложечка для чай
			  aud:: 3
			- #ATM Bendigo  комиссия за 50 aud
			  aud:: 3
	- ### September
	  collapsed:: true
		- Месяц September 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Sep 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-09-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-09-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-09-02]]
		  id:: 39332310-93fa-4743-ae97-0b40d517d96f
		  collapsed:: true
			- #shopping #[[ALDI]] Цветы, печенье
			  aud:: 32.22
			- #shopping #pharmacy Фолиевая кислота
			  aud:: 25.95
		- [[2025-09-03]]
		  id:: 6d296863-098f-46c5-9167-91a4532f1609
		  collapsed:: true
			- #food #take-away Горячий шоколад и 3 печенье 12.70 AUD
			  aud:: 12.70
			- #delivey 2 WaterFloss Waterpik
			  aud:: 332
		- [[2025-09-04]]
		  id:: 5c55bb94-96b4-47b1-89e7-e0db3459ba8c
		  collapsed:: true
			- #shopping #Bunnings Переходник для розетки
			  aud:: 8.95
			- #shopping #[[Woolworths]] Цветы, Кокосовые сливки, 2х TimTam
			  aud::
		- [[2025-09-05]]
		  id:: d9e7f6e7-0424-402c-ad98-88f5502d0ce9
		  collapsed:: true
			- #subscription #ChatGPT
			  idr:: 350000
			  aud:: 0
		- [[2025-09-06]]
		  id:: 2bd1b583-bd0c-4dcf-b049-fb7d50fe9b22
		  collapsed:: true
			- #food Ужин в #HOTA
			  aud:: 23
			- #shopping #[[Woolworths]] - цветы, 3 печенья, кокосовые сливки
			  aud:: 43.75
		- [[2025-09-08]]
		  id:: 43fb96a7-3917-435a-a282-0d398ea2fcd7
		  collapsed:: true
			- #shopping #[[ALDI]] - Ромашковый чай, печенье, сыр, торт
			  aud:: 42.90
			- #shopping Букет и свеча
			  aud:: 190.95
		- [[2025-09-10]]
		  id:: 24997c43-2de6-4f65-a01e-1892b829104d
		  collapsed:: true
			- #pharmacy Глутамин, Брахми, Ашваганда
			  aud:: 81.47
			- #shopping #[[Coles]] Сыр Tasty, Кофе, Изюм
			  aud:: 14.20
			- #delivey 2x AlphaGPC online
			  aud:: 90.09
		- [[2025-09-11]]
		  id:: 478133a1-f44a-484d-816c-6ec9fc41059d
		  collapsed:: true
			- #shopping limonade
			  aud:: 5
			- #shopping limonade RedBull
			  aud:: 4.3
			- #shopping mousepad, cable
			  aud:: 40
		- [[2025-09-12]]
		  id:: 09f22202-1405-47b3-819f-c71b2330915d
		  collapsed:: true
			- #subscription #DeployHQ
			  idr:: 184484
			- #subscription #Manus-AI
			  idr:: 322478
			- #shopping iPhone battery
			  aud:: 80
			- #food Cafe Max Brener
			  aud:: 29.40
		- [[2025-09-13]]
		  id:: 1817f328-2667-43b4-a80e-5cab06869586
		  collapsed:: true
			- #fix iPhone back glass
			  aud:: 149
			- #shopping iPhone transparent case
			  aud:: 25
			- #food Вьетнамские ролы
			  aud:: 12.89
			- #shopping #[[Woolworths]] Лилии, лимонад
			  aud:: 21.81
		- [[2025-09-14]]
		  id:: 4fe5014d-6eed-4296-9cbd-269d1ca97260
		  collapsed:: true
			- #food Детский лимонад с печеньем
			  aud:: 0.50
			- #taxi #Didi #[[ASMY]]
			  aud:: 16.47
			- #food Газированный кокос
			  aud:: 4
			- #donation #[[ASMY]] #Kirtan
			  aud:: 10
			- #taxi #Didi #2Santabelle
			  aud:: 28
		- [[2025-09-15]]
		  id:: 1965c6d4-5913-4717-9ebd-bcd671746720
		  collapsed:: true
			- #shopping #[[ALDI]] - миндаль, кешью, молоко, бананы
			  aud:: 33.10
			- #shopping #[[Woolworths]] - кофе, сливки, сыр Extra Tasty
			  aud:: 14.95
		- [[2025-09-16]]
		  id:: 0da1ccde-dfae-4428-ab17-330294bb86eb
		  collapsed:: true
			- #barbershop
			  aud:: 35
			- #shopping #Choice Конверты
			  aud:: 3
			- #shopping #[[ALDI]] Лимонад
			  aud:: 2
			- #taxi #Didi #Pacific-Fair
			  aud:: 11.30
			- #shopping #Zara Худи и кофта
			  aud:: 156
			- #food Pide
			  aud:: 14
			- #shopping #Sketchers Ботинки
			  aud:: 190
			- #taxi #Didi #2Santabelle
			  aud:: 13
			- #taxi #Pacific-Fair #2Santabelle Оплатил наличкой
			  aud:: 20
		- [[2025-09-17]]
		  id:: d4d3f9b0-1ced-4a2c-8ae2-457ebbbf8870
		  collapsed:: true
			- #shopping Skechers
			  aud:: 180
			- #shopping UniQlo - накидка
			  aud:: 50
			- #taxi #Didi #2Santabelle
			  aud:: 20
		- [[2025-09-18]]
		  id:: d8b19a0b-ce47-47d3-bb56-5e9ade1d690f
		  collapsed:: true
			- #vaccine Whooping Cough and Consultation
			  aud:: 95
			- #food Quiche and Latte
			  aud:: 14
			- #shopping #[[Woolworths]] #flowers magazine headphones
			  aud:: 50
		- [[2025-09-19]]
		  id:: f7703c8c-d270-474e-bd9c-196ca2fb8671
		  collapsed:: true
			- #subscription Claude - Pro Plan
			  aud:: 34
		- [[2025-09-20]]
		  id:: 8ca7e33d-a488-4c14-baf1-9146a93903b6
		  collapsed:: true
			- #shopping #[[Woolworths]] Сыр, печенье, открытка
			  aud:: 23.70
			- #shopping #[[Woolworths]] Печенье, гиёза, пироги
			  aud:: 42.90
		- [[2025-09-21]]
		  id:: 72706978-556d-4166-b638-327c05cae325
		  collapsed:: true
			- #food Кафе с Ноел и Слава
			  aud:: 33.32
			- #food Кафе Горячий шоколад и десерт Ноелу
			  aud:: 18.68
			- #donation Наваратри в Ашраме
			  rub:: 5800
		- [[2025-09-23]]
		  id:: 4eae4a79-410a-461b-81c4-ce3a12dfd6d4
		  collapsed:: true
			- #taxi #Uber #[[ALDI]]
			  aud:: 10.20
			- #subscription #Uber подписка на месяц Uber One
			  aud:: 10
			- #shopping #[[ALDI]] - орешки и печенье
			  aud:: 37.41
			- #shopping #[[Woolworths]] - кофе, сливки
			  aud:: 7.20
			- #food #McDonalds драник, фри, чай лате
			  aud:: 12
		- [[2025-09-24]]
		  id:: d37dd705-6e62-49af-9dab-78ce33e8266a
		  collapsed:: true
			- #donation Kirtan
			  aud:: 10
			- #taxi #Didi to #Q-Centre
			  aud:: 9.50
		- [[2025-09-25]]
		  id:: 5d0b1a22-2a3b-4413-8adf-4d5275c67045
		  collapsed:: true
			- #shopping #[[Woolworths]] Сливки
			  aud:: 4
			- #shopping #[[Coles]] Лимонад
			  aud:: 3
		- [[2025-09-26]]
		  id:: abbf0063-8eb0-41a5-9935-a640e7bd0f0c
		  collapsed:: true
			- #shopping #[[Woolworths]] 3 букета и лимонад
			  aud:: 52
		- [[2025-09-27]]
		  id:: 3a4e8fd7-b7e3-4b9e-aecf-458ca0763782
		  collapsed:: true
			- #Mobile-Internet #subscription Amaysim
			  aud:: 30
			- #donation курс Мужская Природа - предоплата
			  rub:: 10000
			- #food Cafe Isla
			  aud:: 57.70
			- #Didi #2Santabelle
			  aud:: 16.70
		- [[2025-09-29]]
		  id:: 7605b8bb-99f6-451b-9513-98f738671c6e
		  collapsed:: true
			- #flight to Melbourne and back
			  aud:: 280
			- #taxi #Didi #Robina
			  aud:: 17
			- #shopping #Robina Lion's Mane
			  aud:: 70.50
			- #shopping #Robina Матча термос и чай
			  aud:: 109
			- #shopping #Robina #[[Woolworths]] бананы, Gyoza, пироги
			  aud:: 35
			- #taxi #Didi #2Santabelle
			  aud:: 22
	- ### October
	  collapsed:: true
		- Месяц October 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Oct 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-10-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-10-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-10-01]]
		  id:: fe0ee43d-fd1a-47c7-8a86-e494575ec60c
		  collapsed:: true
			- #docs Справка о несудимости из Мексики
			  rub:: 19930
		- [[2025-10-02]]
		  id:: 68048891-4506-4b2e-ae80-584a82816cb9
		  collapsed:: true
			- #food #[[Goji Cafe]] Vietnamese Iced Coffee с печеньем
			  aud:: 17
			- #shopping #pharmacy Витамин Ц
			  aud:: 16
			- #shopping #[[Woolworths]] овсянка и кукуруза
			  aud:: 11.40
			- #shopping #[[Coles]] цветы и сливки
			  aud:: 12.40
			- #shopping #[[ALDI]] печенья, орешки и лимонад, пакет
			  aud:: 40
		- [[2025-10-04]]
		  id:: 514ce498-4b27-4326-bb3a-d1c55e09ddad
		  collapsed:: true
			- #food #[[Goji Cafe]]  Веганский бургер и латте
			  aud:: 30.15
			- #book Atomic Workflows
			  aud:: 135
		- [[2025-10-05]]
		  id:: b47a0fa9-3821-4812-b1bd-06b8fcc7cab9
		  collapsed:: true
			- #food #[[Goji Cafe]] Блюдо 2 и капучино
			  aud:: 31
			- #shopping JB Hi-Fi - Insta360 gimbal
			  aud:: 203
			- #shopping #[[ASMY]] Ginger Beer
			  aud:: 4
			- #donation #[[ASMY]] Kirtan
			  aud:: 10
		- [[2025-10-06]]
		  id:: 02457f15-22ea-4862-a925-f2147c903452
		  collapsed:: true
			- #shopping #[[Coles]] момо, вареники, кофе, горячий шоколад, салфетки, тряпочки
			  aud:: 34
		- [[2025-10-07]]
		  id:: c864fb1a-aa25-4e36-8f71-73372e50df2e
		  collapsed:: true
			- #food #[[Goji Cafe]] Завтрак с Матчей и Vegetarian Wrap
			  aud:: 27.60
		- [[2025-10-08]]
		  id:: 999f5583-b0f0-4237-98f3-856586f8b67f
		  collapsed:: true
			- #food Чай латте
			  aud:: 4.15
			- #bus Даблдекер из Аэропорта в Мельбурн Сити
			  aud:: 25
			- #food Обед в Hubert Bistro - салат с халуми, caramel slice, 2 chai late
			  aud:: 35.10
			- #study Soundstrue - IFS
			  aud:: 170
		- [[2025-10-09]]
		  id:: 580838a6-42d9-4bc8-ad24-6ffae956bf2a
		  collapsed:: true
			- #food Кофе лате
			  aud:: 5
			- #food Potato Twister
			  aud:: 11.20
			- #food Кофе лате и капучино
			  aud:: 10
			- #shopping кошелёк для мелочи
			  aud:: 10
			- #food Chai Latte
			  aud:: 5
			- #shopping магазин Vinnies Носки
			  aud:: 5
			- #shopping #[[Coles]] Сливки и соевый фарш
			  aud:: 13.50
		- [[2025-10-10]]
		  id:: c4a013d1-0302-40f5-b2e0-2e6b6f7d44b7
		  collapsed:: true
			- #study Книга - No Bad Parts
			  aud:: 30
			- #study Аудио - Greater than the Sum of our Parts 65 AUD
			  aud:: 65
			- #food кафе Cafe Koochino - чай лате и лемон тарт
			  aud:: 11.60
		- [[2025-10-11]]
		  id:: c281f656-62a0-467a-9bd7-c7cc6459f55d
		  collapsed:: true
			- #food shop Salvos - сладости Fresh raspberry Lacorice
			  aud:: 3.50
			- #food кафе Mordi Canteen - эспессо с мороженным Affogato
			  aud:: 7.15
		- [[2025-10-12]]
		  id:: aa1e632d-2c82-428e-aa7d-31dc6126ea37
		  collapsed:: true
			- #subscription deployHQ
			  idr:: 275000
			- #food Печенье на борту Virgin Airlines
			  aud:: 5.50
		- [[2025-10-13]]
		  id:: 02235cca-39a3-4a79-bcd5-f2f38618cbe9
		  collapsed:: true
			- #subscription domain ayaruna.net 1 year
			  usd:: 24.53
			- #food #[[ALDI]] печенье
			  aud:: 8.20
			- #shopping #[[Woolworths]] Журнал против сладкого, лимонад, шоколад
			  aud:: 24
			- #service Массаж
			  aud:: 100
		- [[2025-10-14]]
		  id:: 7a3c8dfe-7aa6-4c94-80f1-47c84ae3cde1
		  collapsed:: true
			- #food Завтрак в #[[Goji Cafe]] - wrap и Мате
			  aud:: 27.61
			- #food Матча в #[[Goji Cafe]]
			  aud:: 6.19
			- #subscription Google One за год
			  kzt:: 50000
		- [[2025-10-15]]
		  id:: edaf4e17-7e6e-4e8f-9a84-d65ca0a4bd25
		  collapsed:: true
			- #food #[[Goji Cafe]] бургер и матча
			  aud:: 30.60
			- #subscription #CapCut 1 year
			  aud:: 225
			- #service Перевод ID, BC на английский
			  kzt:: 12000
			- #donation #[[ASMY]]
			  aud:: 5
		- [[2025-10-16]]
		  id:: 958d138a-fa83-483c-b8d7-1b21fb9515dd
		  collapsed:: true
			- #food #[[Goji Cafe]] Rosti potato and Matcha
			  aud:: 31.70
			- #service Car wash
			  aud:: 17
			- #food Пиццерия - Pizza Zuzza, Red Bull
			  aud:: 21.90
			- #shopping #[[Coles]] Цветы - лилии и белые
			  aud:: 20
			- #shopping #Choice RedBull
			  aud:: 3.50
		- [[2025-10-17]]
		  id:: ab7f1f8e-919c-4396-90a7-4b92b5dff4d2
		  collapsed:: true
			- #service Обработка фото
			  aud:: 14.95
			- #food #[[ASMY]] Watermelon juice
			  aud:: 4
			- #service Перевод справок из полиции
			  kzt:: 15500
		- [[2025-10-18]]
		  id:: 4c798126-38d1-4dce-888f-12b99c437802
		  collapsed:: true
			- #food Кафе - ромашковый чай с мёдом
			  aud:: 3.70
		- [[2025-10-19]]
		  id:: 14d753cc-60ce-401f-b481-30f4c55ddd54
		  collapsed:: true
			- #shopping #HOTA-Market Сушеные бананы
			  aud:: 7.20
			- #shopping #HOTA-Market Хлеб без глютена
			  aud:: 13
			- #food #HOTA-Market Сок Маракуя медиум
			  aud:: 5
			- #shopping #Bunnings 4 AAA батарейки
			  aud:: 2
			- #food #[[ASMY]] Sparkling Coco
			  aud:: 4
			- #donation #[[ASMY]] Kirtan
			  aud:: 10
		- [[2025-10-20]]
		  id:: 29897fc4-080b-494d-95ef-00b2749c5ed3
		  collapsed:: true
			- #food #[[Goji Cafe]] Wrap & Match
			  aud:: 27.70
			- #subscription #claude 1 month
			  aud:: 34
			- #barbershop [[Q Centre]]
			  aud:: 35
			- #shopping #[[ALDI]] almonds, ice tea, hazelnut latte, v energy
			  aud:: 21.30
		- [[2025-10-21]]
		  id:: 6d3cd6d9-9121-4527-b4da-17f76f7af2df
		  collapsed:: true
			- #shopping #[[Woolworths]] бананы, coconut milk, coconut cream, redbull, IceTea Peach
			  aud:: 22.1
		- [[2025-10-22]]
		  id:: 92272853-d58d-4f34-b603-1f35c73c0416
		  collapsed:: true
			- #shopping #[[Woolworths]] Lipton, bananas
			  aud:: 6.80
			- #food #[[Goji Cafe]] Rosti Potato, Matcha
			  aud:: 31.70
			- #foode #[[ASMY]] Шоколад с напитком
			  aud:: 12
			- #donation #[[ASMY]]
			  aud:: 5
		- [[2025-10-23]]
		  id:: 5b0cdca6-167a-4e5e-a46f-898fbdcd4864
		  collapsed:: true
			- #food #Tower-28-cafe Matcha, Cookies
			  aud:: 21.60
		- [[2025-10-24]]
		  id:: f876a7c8-339b-4ddb-baf5-23e445558490
		  collapsed:: true
			- #shopping #[[Woolworths]] Sweetener Monk fruit, V energy
			  aud:: 11.15
			- #food Mango Lassi and Fried Vegs
			  aud:: 10
			- #food Mango Lassi
			  aud:: 5
			- #food Cafe at Brisbane Plaza White Chocolate Matcha
			  aud:: 9.50
			- #food Water at Gas Station
			  aud:: 4
		- [[2025-10-25]]
		  id:: ebc1709b-df5e-47d5-b730-b0a90d604bc4
		  collapsed:: true
			- #food Матча и пирожное
			  aud:: 11.90
		- [[2025-10-26]]
		  id:: 9af9cf05-2de9-4b53-8ec9-d9bb99ae1dce
		  collapsed:: true
			- #food #HOTA-Market Medium passion fruit juice
			  aud:: 5
			- #shopping #HOTA-Market Dried bananas
			  aud:: 10.40
			- #food #[[ASMY]] Шоколад и лимонад
			  aud:: 12
			- #donation #[[ASMY]]
			  aud:: 5
			- #shopping #litres Энтони Робинс - Разбуди в себе исполина
			  aud:: 10
		- [[2025-10-27]]
		  id:: a2aa48e9-d0b4-4a65-b748-b2a2f8d5c4f2
		  collapsed:: true
			- #subscription Amaysim за 28 дней
			  aud:: 30
			- #debt отдал за бензин
			  aud:: 100
			- #shopping #[[Woolworths]] цветы, горячий шоколад, наушники
			  aud:: 48
		- [[2025-10-28]]
		  id:: c2bfb148-43e2-4561-99e7-be8d01f8d6cc
		  collapsed:: true
			- #food #[[Goji Cafe]] Rosti and Match
			  aud:: 31.70
			- #food #[[Goji Cafe]] Brownie Cheesecake
			  aud:: 8.50
			- #subscription iCloud+ with 50 GB
			  aud:: 1.5
		- [[2025-10-29]]
		  id:: 4c0c15fd-f04e-44b3-b56b-157aaedb0eef
		  collapsed:: true
			- #service Переводы справок из KompAS на Казахский
			  kzt:: 23000
			- #service Переводы справок из KompAS на Английский
			  kzt:: 25000
		- [[2025-10-30]]
		  id:: c23b452e-4915-4314-9343-a36cb04454e5
		  collapsed:: true
			- #shopping 3 Oat milk
			  aud:: 6.80
		- [[2025-10-31]]
		  id:: 7fde9df4-124f-4983-973f-f24ae20d2880
		  collapsed:: true
			- #subsription Академия [[Прем Баба]]
			  idr:: 634500
			  aud:: 0
			- #donation Махешику за ноября
			  rub:: 5500
	- ### November
	  collapsed:: true
		- Месяц November 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Nov 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-11-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-11-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-11-01]]
		  id:: 88a5678a-2603-449e-9198-c100444ac25a
		  collapsed:: true
			- #food Мороженое White Magnum
			  aud:: 6
			- #shopping Матча, сыр, хлеб
			  aud:: 56
			- #service Ai summit from Tony Robbins
			  usd:: 117
		- [[2025-11-02]]
		  id:: 41d6e842-5a69-4e3d-85b5-4b3eb539107d
		  collapsed:: true
			- #food #[[Goji Cafe]] Smoothie - Watermelon and Lemon
			  aud:: 10
			- #food #[[Goji Cafe]] Smoothie - Banana and Chocolate
			  aud:: 10
			- #food #[[ASMY]] Sparkling coconut
			  aud:: 4
			- #donation #[[ASMY]]
			  aud:: 5
		- [[2025-11-03]]
		  id:: 5f417567-1ed1-46ba-94cc-cf3171491c50
		  collapsed:: true
			- #food #[[Goji Cafe]] Wrap and Matcha
			  aud:: 29
			- #service Medical comission
			  aud:: 392
			- #shopping Milk Thermometer
			  aud:: 10
			- #food 2 black rise salad
			  aud:: 24
			- #food Кише и горячий шоколад
			  aud:: 17
			- #food Lemonade
			  aud:: 4
			- #shopping Shopping Amazon - Mag Safe PowerBank 10k mah
			  aud:: 73
		- [[2025-11-04]]
		  id:: 63a02b84-d616-4be4-8dde-54c32b1c0fb8
		  collapsed:: true
			- #food #Tower-28-cafe Rosti and Matcha Oat
			  aud:: 31.30
			- #food #Goldies-Cafe Orange juice
			  aud:: 4.50
			- #shopping #pharmacy L Theanin
			  aud:: 30.30
			- #shopping #amazon Наушники маме на Рождество
			  aud:: 40
		- [[2025-11-05]]
		  id:: 3dafab2b-9e3d-4473-b9a4-4322e59da843
		  collapsed:: true
			- #food Smoothie watermelon lemon and topping
			  aud:: 14
			- #shopping #pharmacy - Omega3, Creatine, Перга, Железо
			  aud:: 136.20
			- #donation #[[ASMY]]
			  aud:: 5
		- [[2025-11-06]]
		  id:: f10dc8a7-0f26-421c-9099-45ca91fd0197
		  collapsed:: true
			- #shopping #[[ALDI]]  чай, v energy, бананы, миндаль, oat milk, печенье
			  aud:: 25
			- #food #[[Goji Cafe]] burger and Match oat milk
			  aud:: 31.20
			- #service decodo proxy
			  aud:: 6.5
		- [[2025-11-07]]
		  id:: 2c79c051-06f0-4263-8488-05a152d3ff60
		  collapsed:: true
			- #shopping Лимонад и киндер
			  aud:: 9.50
			- #shopping Лимонад и чай
			  aud:: 4.60
			- #service Decodo proxy
			  aud:: 4.80
			- #food #[[ASMY]] шоколад
			  aud:: 8
			- #donation #[[ASMY]] Kirtan
			  aud:: 5
		- [[2025-11-08]]
		  id:: c95d29b8-9c84-4708-8e43-a65d1b653bde
		  collapsed:: true
			- #subsription Tinder
			  aud:: 36
			- #subsription SoundTrue IFS
			  aud:: 138.50
			- #food Матча и чипсы в кафе с фильмом на пляже
			  aud:: 15
		- [[2025-11-09]]
		  id:: 67017083-ca4e-41f0-87a8-47f56cbb44f0
		  collapsed:: true
			- #food #[[ASMY]] Шоколад и лимонад
			  aud:: 12
			- #donation #[[ASMY]]
			  aud:: 10
		- [[2025-11-10]]
		  id:: 26d982ae-2f0f-4c97-9c1b-3bbf5501df96
		  collapsed:: true
			- #food #[[Goji Cafe]] Ромашка и рости
			  aud:: 30.50
			- #food #[[Goji Cafe]] Мафин
			  aud:: 5.20
			- #food #Santctum-Cafe Матча и пирожное
			  aud:: 20.30
			- #food #Santctum-Cafe Ice Matcha
			  aud:: 10
			- #shopping Книжный Classical Philosophy
			  aud:: 7
		- [[2025-11-11]]
		  id:: d1476af1-6c41-413e-b548-19726bf3bbf4
		  collapsed:: true
			- #food #711 2 v energy и киндер
			  aud:: 9.50
			- #shopping #[[Woolworth]] цветы, сливки, печенье
			  aud:: 44.40
			- #service Tinder
			  aud:: 56
		- [[2025-11-12]]
		  id:: a010ed7c-b0ba-46d8-a9a1-e9d4f232db1d
		  collapsed:: true
			- #donation #[[ASMY]]
			  aud:: 5
			- #subsription DeployHQ
			  aud:: 24
		- [[2025-11-13]]
		  id:: 0743985a-de4a-4481-a85a-7b233c8020a6
		  collapsed:: true
			- #food #[[Goji Cafe]] Бургер и Oat Matcha
			  aud:: 31.50
			- #shopping #[[ALDI]] - 2 v energy, ice tea
			  aud:: 7.20
			- #Gasoline #[[Haval]] 98
			  aud:: 119.33
			- #subsription #Claude-AI claude Max
			  aud:: 154.50
			- #shopping #711 шоколад Twix с зелёным чаем
			  aud:: 3
			- #Курс #Tony-Robbins Robbins Manades
			  aud:: 56
		- [[2025-11-14]]
		  id:: 2909a970-de90-41c1-8269-0e213bfc403d
		  collapsed:: true
			- #food #[[Goji Cafe]] Завтрак Rosti Match oat milk
			  aud:: 32.70
			- #shopping #[[ALDI]] чай, печенье, v energy, орешки
			  aud:: 40
			- #donation #[[ASMY]]
			  aud:: 5
		- [[2025-11-16]]
		  id:: 84eb5cc3-780c-4935-ba68-7e2ec32983b4
		  collapsed:: true
			- #food #[[Goji Cafe]] Завтрак wrap, matcha oat milk
			  aud:: 28.20
			- #food #[[Goji Cafe]] Smoothie
			  aud:: 10.15
			- #food #[[ASMY]] Lemonade
			  aud:: 4
			- #donation #[[ASMY]]
			  aud:: 5
			- #subsription 3 месяца в #[[ASMY]]
			  aud:: 99
		- [[2025-11-17]]
		  id:: dc5f568d-2a6f-4463-aaac-5af484e32196
		  collapsed:: true
			- #food #[[Goji Cafe]] Matcha oat milk
			  aud:: 07.20
			- #rent Yoga Mat #[[ASMY]]
			  aud:: 2
		- [[2025-11-18]]
		  id:: 0916cf32-bae3-4ac4-be76-6f337e038a3c
		  collapsed:: true
			- #shopping #[[ASMY]] коврик
			  aud:: 40
			- #food Cafe Black Swan - Матча
			  aud:: 5.50
			- #Курс Мужская Природа
			  rub:: 37000
		- [[2025-11-19]]
		  id:: 45cdab7d-c2a1-4073-a3d6-34ef235ce21b
		  collapsed:: true
			- #food #[[Goji Cafe]] Matcha oat milk
			  aud:: 7.20
			- #barbershop Haircut
			  aud:: 35
			- #shopping #[[ALDI]] Апельсиновый сок, молоко, 2 v energy, Nori
			  aud:: 14.90
		- [[2025-11-21]]
		  id:: 9d6c7f62-da1e-4740-adaf-02ce67a53ef7
		  collapsed:: true
			- #shopping #[[Coles]] хумус, сахар
			  aud:: 15.50
		- [[2025-11-22]]
		  id:: cdb89dfd-f0a9-48a4-88a3-452e6d84c2c2
		  collapsed:: true
			- #shopping - #[[ALDI]] - Бананы, хлебцы, Ice Tea
			  aud:: 5.55
			- #subsription Macincloud - 25 hours
			  aud:: 45
			- #subsription megahost.kz за VPS
			  kzt:: 2080
		- [[2025-11-23]]
		  id:: 7e24104d-2910-49d1-9656-2031d21264be
		  collapsed:: true
			- #food - [[Goji Cafe]] - Matcha and Carot Cake
			  aud:: 14.20
			- #food - [[Goji Cafe]] - Camomile tea
			  aud:: 5.50
			- #food - #[[ASMY]] - Lemonade
			  aud:: 4
		- [[2025-11-24]]
		  id:: 6ad06037-e286-4573-b6ae-4cf9ded923d2
		  collapsed:: true
			- #subsription  Amaysym
			  aud:: 30
		- [[2025-11-25]]
		  id:: acdb9483-65cf-43ee-a7cb-2091400a7135
		  collapsed:: true
			- #food - 2 v energy and KitKat
			  aud:: 8.50
			- #food - [[Woolworth]] - цветы, кофе, бананы, сливки
			  aud:: 45.75
		- [[2025-11-26]]
		  id:: b5a284bf-f1c0-48fd-8d7b-06dd3f550b6b
		  collapsed:: true
			- #subsription Apple Developer Program - Membership for one year
			  aud:: 150
			- #shopping #[[Coles]] -  v energy, растительное молоко х3
			  aud:: 12.55
			- #subscription Prembaba Academy
			  idr:: 636000
		- [[2025-11-27]]
		  id:: b3cf31b9-ced7-47c7-a1fa-8f4e0df3f6b8
		  collapsed:: true
			- #shopping #[[Coles]] V energy
			  aud:: 2.95
		- [[2025-11-28]]
		  id:: b6b6f55d-e8c3-41c7-b790-c283bce96d10
		  collapsed:: true
			- #shopping #[[ALDI]] орешки 2, печенье
			  aud:: 17.65
			- #shopping #[[Coles]] V energy
			  aud:: 3
			- #food #[[ASMY]] Лимонад с MnMs
			  aud:: 13
			- #shopping Для похода
			  aud:: 275
			- #food Indian food на горе Tamborine
			  aud:: 18
		- [[2025-11-29]]
		  id:: ba83881b-7e2b-4db5-893f-e65237265ca2
		  collapsed:: true
			- #food #[[Goji Cafe]] Big Boss Breakfast
			  aud:: 42.20
			- #food #[[Goji Cafe]] Лимонад
			  aud:: 7
			- #shopping Sunscreen
			  aud:: 20
			- #shopping Палатка (Tentworld) и подставка
			  aud:: 550
			- #shopping Снеки #[[Woolworth]] - яблоки, орешки, Гранола Бар, вода 2л, лимонад
			  aud:: 23.80
			- #shopping #Bunnings Дождевик
			  aud:: 2.50
			- Ринату для Тани
			  kzt:: 300000
			- Camping (Thunderbird Park)
			  aud:: 72
		- [[2025-11-30]]
		  id:: 198a06fd-3847-4bc8-bde7-ce952482e24b
		  collapsed:: true
			- #food Буфет
			  aud:: 35
			- #food Carob Bear
			  aud:: 2.50
	- ### December
	  collapsed:: true
		- Месяц December 2025
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD Dec 2025"]
			    :query [
			      :find (sum ?n)
			      :with ?b
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?name]
			        [(clojure.string/starts-with? ?name "2025-12-")]
			    ]
			    :view (fn [rows] [:div (/ (int (+ (* (first rows) 100) 0.5)) 100.0)])
			  }
			  #+END_QUERY
		- По дням
		  collapsed:: true
			- #+BEGIN_QUERY
			  {
			    :title [:p "AUD по дням"]
			    :query [
			      :find ?date (sum ?n)
			      :keys date aud
			      :where
			        [?b :block/properties ?prop]
			        [(get ?prop :aud) ?v]
			        [(* 1 ?v) ?n]
			        [?b :block/parent ?parent]
			        [?parent :block/refs ?ref]
			        [?ref :block/name ?date]
			        [(clojure.string/starts-with? ?date "2025-12-")]
			    ]
			    :view (fn [rows]
			      [:table {:style {:width "100%"}}
			        [:thead
			          [:tr
			            [:th {:style {:text-align "left" :padding "8px"}} "Дата"]
			            [:th {:style {:text-align "right" :padding "8px"}} "AUD"]]]
			        [:tbody
			          (for [r (sort-by :date rows)]
			            [:tr
			              [:td {:style {:padding "8px"}} (:date r)]
			              [:td {:style {:text-align "right" :padding "8px"}} (/ (int (+ (* (:aud r) 100) 0.5)) 100.0)]])]])
			  }
			  #+END_QUERY
		- [[2025-12-01]]
		  id:: 842f5390-08a2-4522-9b58-19fe3e91a0ed
		  collapsed:: true
			- #food Кокао
			  aud:: 5
			- #shopping #[[Coles]] v energy
			  aud:: 2.95
		- [[2025-12-02]]
		  id:: 909950dc-8e85-4382-816d-f3405a135d96
		  collapsed:: true
			- #food #[[Woolworths]] хризантемы сливки лимонад
			  aud:: 23.85
			- #food Пицца
			  aud:: 19.90
		- [[2025-12-03]]
		  id:: 9cd04de4-8ced-4f00-a6aa-a85d392577b6
		  collapsed:: true
			- #food Завтрак Haloumi Wrap, Matcha
			  aud:: 21.70
			- #food Cocao #Goldie's
			  aud:: 4.70
		- [[2025-12-04]]
		  id:: cf9d5aa6-7201-4b9c-8cd5-0cd2bcf92b12
		  collapsed:: true
			- #food Завтрак Бургер и Матча
			  aud:: 31.20
			- #shopping #[[ALDI]] печенье, молоко, чай, энергетик, кускус
			  aud:: 18.70
		- [[2025-12-05]]
		  id:: 5db1aa11-7f05-4084-95c2-dd39a6e56aed
		  collapsed:: true
			- #food #[[ASMY]] Лимонад
			  aud:: 4
			- #shopping Kapha Tea
			  aud:: 10
		- [[2025-12-06]]
		  id:: 8a35ef10-9720-4822-9318-997070452c8a
		  collapsed:: true
			- #shopping #[[Woolworths]] Яблоки, вода, Гранола, молоко лимонад
			  aud:: 17.05
			- #shopping #Bunnings Дрова
			  aud:: 20
		- [[2025-12-07]]
		  id:: 88ea2f6f-8477-4205-9cc8-ea053ce55f0b
		  collapsed:: true
			- #camping Оплата за Ночлег
			  aud:: 15
			- #food на ферме Альпак - горячий шоколад
			  aud:: 6
			- #shopping на заправке - V energy
			  aud:: 6.95
			- #shopping #[[ASMY]] Лимонад и Гранола
			  aud:: 6.50
		- [[2025-12-08]]
		  id:: 6541152a-75cf-43d1-b7a9-46add3f57478
		  collapsed:: true
			- #consulting Оплата консультации Анна Заикина
			  kzt:: 172000
			- #shopping Магазин на заправке - Лимонад и шоколад
			  aud:: 11
			- #shopping #[[Coles]] Цветы, бананы, сыр, лимонад
			  aud:: 44.75
			- #subsription SoundsTrue IFS Schwartz
			  aud:: 150
			- #service Оплата за перевод 52000 KZT
			  aud:: 155
		- [[2025-12-09]]
		  id:: 276d6a7d-b034-4d8f-b6fc-3960509ce9d0
		  collapsed:: true
			- #shopping Магазин на заправке - Лимонад и шоколад
			  aud:: 11
			- #shopping #[[ALDI]] Лимонад, шоколад, чай, печенье, v energy
			  aud:: 12.45
			- #food #Goldie's Vegi stack and hot chocolate
			  aud:: 15.40
			- #service Перевод документов на Английский
			  aud:: 62
			- #shopping чай Oriental Beauty из [[Бали]]
			  aud:: 535
		- [[2025-12-10]]
		  id:: a60a51e9-d39e-467e-ad53-237532fea92b
		  collapsed:: true
			- #shopping #[[ALDI]] Лимонад, печенье, молоко
			  aud:: 9.40
		- [[2025-12-11]]
		  id:: 269a49a7-13e9-4216-a949-d55169a14103
		  collapsed:: true
			- #service privorot24.com from Permata
			  idr:: 593909
			- #shopping #[[Coles]] Лимонад, пенка, подстригалка для носа
			  aud:: 23
		- [[2025-12-12]]
		  id:: 338e74cf-7f90-477f-bff5-2e519f0dd8e9
		  collapsed:: true
			- #shopping Магазин у заправки - 2 лимонада и шоколад
			  aud:: 13.40
			- #food [[Goji Cafe]] - Warp and Matcha
			  aud:: 26.20
			- #subsription DeployHQ
			  idr:: 266000
		- [[2025-12-13]]
		  id:: 0c95bcdb-20fb-4611-a9e0-e2dc36cf41a6
		  collapsed:: true
			- #food [[Goji Cafe]] - Rosti potato and Matcha
			  aud:: 31.80
			- #food Брауни
			  aud:: 5
			- #food Магазин 2 лимонада, шоколад и вода
			  aud:: 14.60
			- #accomodation Ночлег Binna Burra
			  aud:: 35
			- #food Lasagna
			  aud:: 25
		- [[2025-12-14]]
		  id:: 6ea6bdee-4656-4773-b1a5-e65cabd2e64d
		  collapsed:: true
			- #food Завтрак с кофе - Binna Burra Tea House
			  aud:: 23.80
			- #food 2 лимонада и шоколад
			  aud:: 11
			- #shopping #JB-HiFi Sensibo
			  aud:: 130
			- #shopping #JB-HiFi Insta selfie stick
			  aud:: 50
			- #food Шоколад
			  aud:: 4.60
			- #food Лимонад и печенье
			  aud:: 6.50
		- [[2025-12-15]]
		  id:: 3f2b1d4f-30ec-4f11-aa18-54aec3f68ae1
		  collapsed:: true
			- #food Лимонад и шоколад
			  aud:: 14
		- [[2025-12-16]]
		  id:: 3daa1c1f-78eb-4968-b8ce-97097808df08
		  collapsed:: true
			- #servise Spa
			  aud:: 310
			- #food магазин возле Spa - 2 лимонада и шоколад
			  aud:: 16.40
			- #food Ice tea, кускус, горячий шоколад, ромашка
			  aud:: 10.85
		- [[2025-12-17]]
		  id:: d828a1e4-064c-46f2-9ea7-ae41cd8d7fcc
		  collapsed:: true
			- #transport Бензин
			  aud:: 104.45
			- #subsription Claude
			  aud:: 170
			- #food Veggie burger, fries and Bundaberg @ Uncles cafe
			  aud:: 21
		- [[2025-12-18]]
		  id:: 87099cd4-a05e-4aeb-a772-70af3e2e55ce
		  collapsed:: true
			- #food 2 лимонада и шоколад
			  aud:: 11
		- [[2025-12-19]]
		  id:: 316470c0-2d91-4995-bcfd-2ea925d387e1
		  collapsed:: true
			- #food 2 лимонада
			  aud:: 4.10
			- #other Цветы
			  aud:: 18
			- #food Лимонад
			  aud:: 4
			- #food Лимонад и печенье
			  aud:: 12.30
		- [[2025-12-20]]
		  id:: 97e7be77-545b-4540-aee8-a3fb726b2669
		  collapsed:: true
			- #other Ночлег
			  aud:: 15
		- [[2025-12-21]]
		  id:: 12fc65fb-42ff-48fd-8d16-388953ad6ad3
		  collapsed:: true
			- #food ферма альпак - Завтрак пицца и зеленый чай
			  aud:: 33
			- #shopping Магазин на заправке - 2 лимонада, 2 шоколада
			  aud:: 15.40
			- #food Магазин на заправке - Лимонад и шоколад
			  aud:: 5.20
		- [[2025-12-22]]
		  id:: b5164cbb-d8ac-426f-8bb0-a2ddb7f9e596
		  collapsed:: true
			- #shopping #[[ALDI]] Бананы, 2 печенье, орехи, энергетик, ice tea
			  aud:: 24.10
			- #food #[[Goji Cafe]] No piggy Bun and Matcha latte
			  aud:: 31.20
			- #subsription Amaysim
			  aud:: 30
		- [[2025-12-23]]
		  id:: 7042331a-1938-4cea-afba-e3fb5f8026a2
		  collapsed:: true
			- #subsription Amaysim
			  aud:: 30
			- #food #Seven11 2 шоколада и 2 энергетика
			  aud:: 16.50
			- #shopping Чайник, печеньки с предсказаниями и с дурианом
			  aud:: 32.17
			- #food Бургер с фри и ice tea
			  aud:: 21.50
		- [[2025-12-24]]
		  id:: 493f8123-2924-4163-baca-191591cfa3a8
		  collapsed:: true
			- #food Завтрак в аэропорту чай и фри
			  aud:: 8.50
			- #shopping #[[Woolworths]] Овсянка, шоколад, печенье, сок, чай
			  aud:: 26.90
		- [[2025-12-26]]
		  id:: a3795ab3-f710-431e-937c-9f0a8bbe7d88
		  collapsed:: true
			- #food Сок, лимонад, шоколад
			  aud:: 17.95
		- [[2025-12-27]]
		  id:: 5586cc84-2e19-4efa-8d35-7fcb9948cc01
		  collapsed:: true
			- #guitar Курс по гитаре
			  rub:: 8390
			  aud:: 160
			- #shopping Фигурка ангела
			  aud:: 18.50
			- #barbershop #shaving Стрижка и бритье
			  aud:: 55
			- #shopping Кубик и карты
			  aud:: 12
			- #food Шоколад
			  aud:: 1
		- [[2025-12-28]]
		  id:: c6e301fd-1863-4e80-a297-eab07ee6a7ba
		  collapsed:: true
			- #food Обед (пирог, матча, карот кейк)
			  aud:: 22.60
			- #food Лимонад и шоколад
			  aud:: 15
		- [[2025-12-29]]
		  id:: b3531cc5-6a00-4ec4-9495-2f18e0ba8925
		  collapsed:: true
			- #food Ресторан
			  aud:: 47
			- #other Билет в Музей скульптур
			  aud:: 15
		- [[2025-12-30]]
		  id:: ee80242d-13f2-42a0-8afb-cb65026cf471
		  collapsed:: true
			- #food Лимонад, шоколад, сок
			  aud:: 11.25
			- #subsription OnlyFans
			  usd:: 16.50
			  aud:: 25
		- [[2025-12-31]]
		  id:: 972f6e1e-71b2-4108-ab2c-24213f622ff3
		  collapsed:: true
			- #food Лимонад и шоколад
			  aud:: 6.20