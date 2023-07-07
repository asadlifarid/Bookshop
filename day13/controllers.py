from flask import render_template, request, redirect
from app import app
from models import *
from forms import *


# category = ['3D KITAB', 'AKADEMIK', 'BƏDII', 'BIZNES', 'DETEKTIV']

# recommended_items = {
#     1 : {
#         'id' : 1,
#         'name' : 'Kim deyir ki, bacarmazsan?!',
#         'author' : 'Deniel Çidiak',
#         'price' : 5.99,
#         'quantity': 3,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'TEAS press',
#         'description' : 'Deniel Çidiak bir gün öz həqiqətini yaşamadığını dərk edib və həmin gün onun həyatının dönüş nöqtəsi olub. İşindən yarımır, başqaları ilə münasibətlərindən əziyyət çəkirmiş. Gerçək dəyərləri ilə səsləşməyən seçimləri onun həyatını ağırlaşdırırmış. Lakin o, içində yatan, – və əslində hamımıza xas olan, – gizli potensialını dərk edə bilmirmiş. Beləcə, öz daxili aləminə böyük səyahətə başlayıb. ',
#         'image' : 'book1.jpeg'
#     },

    
#     3 : {
#         'id' : 3,
#         'name' : 'Sən həyatını yaxşılaşdıra bilərsən',
#         'author' : 'Luiza Hey',
#         'price' : 20.99,
#         'quantity': 1,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : 'Əgər siz "Sən həyatını yaxşılaşdıra bilərsən" kitabında verilən çalışmaları qarşınıza çıxdıqca yerinə yetirsəniz, kitabı hələ oxuyub qurtarmamış həyatınızı dəyişməyə başlayacaqsınız. Tövsiyə edirəm ki, kitabı bir dəfə nəzərdən keçirəndən sonra onu yenidən diqqətlə oxuyasınız, lakin bu dəfə hər bir çalışmanı dostunuzla və ya ailə üzvlərinizdən biri ilə tələb olunduğu kimi yerinə yetirin. Bilin ki, bu kitabdakıları yerinə yetirərkən mənim sevgimi həmişə hiss edəcəksiniz. Luiza Hey',
#         'image' : 'book3.jpeg'

#     },


#     5 : {
#         'id' : 5,
#         'name' : 'Şirin portağal ağacım',
#         'author' : 'Joze Mauru di Vaskonselos',
#         'price' : 10,
#         'quantity': 2,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : '“Yalnız uşaqlar nə axtardıqlarını bilirlər”, – deyirdi Eqzüperi. Biz bu həqiqəti “Şirin portağal ağacım”da balaca Zezenin timsalında görürük. Zeze kasıb bir ailənin dəcəl uşağı olsa da, qəlbi günəş kimi parlaq və insan sevgisiylə doludur.',
#         'image' : 'book5.jpeg'

#     }
# }







# book_list = {
#     1 : {
#         'id' : 1,
#         'name' : 'Kim deyir ki, bacarmazsan?!',
#         'author' : 'Deniel Çidiak',
#         'price' : 5.99,
#         'quantity': 3,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'TEAS press',
#         'description' : 'Deniel Çidiak bir gün öz həqiqətini yaşamadığını dərk edib və həmin gün onun həyatının dönüş nöqtəsi olub. İşindən yarımır, başqaları ilə münasibətlərindən əziyyət çəkirmiş. Gerçək dəyərləri ilə səsləşməyən seçimləri onun həyatını ağırlaşdırırmış. Lakin o, içində yatan, – və əslində hamımıza xas olan, – gizli potensialını dərk edə bilmirmiş. Beləcə, öz daxili aləminə böyük səyahətə başlayıb. ',
#         'image' : 'book1.jpeg'
#     },

    

#     2 :  {
#         'id' : 2,
#         'name' : 'Kürk Mantolu Madonna',
#         'author' : 'Sebahattin Ali',
#         'price' : 3.66,
#         'quantity': 2,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : "Kürk Mantolu Madonna, Sabahattin Ali'nin 1943 yılında yayımladığı bir romanıdır. Kitapta dokunaklı bir aşk hikâyesi anlatılmaktadır.",
#         'image' : 'book2.jpeg'
#     },



#     3 : {
#         'id' : 3,
#         'name' : 'Sən həyatını yaxşılaşdıra bilərsən',
#         'author' : 'Luiza Hey',
#         'price' : 20.99,
#         'quantity': 1,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : 'Əgər siz "Sən həyatını yaxşılaşdıra bilərsən" kitabında verilən çalışmaları qarşınıza çıxdıqca yerinə yetirsəniz, kitabı hələ oxuyub qurtarmamış həyatınızı dəyişməyə başlayacaqsınız. Tövsiyə edirəm ki, kitabı bir dəfə nəzərdən keçirəndən sonra onu yenidən diqqətlə oxuyasınız, lakin bu dəfə hər bir çalışmanı dostunuzla və ya ailə üzvlərinizdən biri ilə tələb olunduğu kimi yerinə yetirin. Bilin ki, bu kitabdakıları yerinə yetirərkən mənim sevgimi həmişə hiss edəcəksiniz. Luiza Hey',
#         'image' : 'book3.jpeg'

#     },

    
#     4 : {
#         'id' : 4,
#         'name' : 'Abşeron yarımadamı',
#         'author' : 'Ramil Əhməd',
#         'price' : 6.99,
#         'quantity': 1,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Libraff',
#         'description' : 'Kitabın redaktoru Aqşin Yeniseydir. Kitab yaxın günlərdə ictimaiyyətə təqdim ediləcək. Qeyd edək ki, “Abşeron yarımadamı” müəllifin beşinci kitabıdır.',
#         'image' : 'book4.jpeg'
#     },


#     5 : {
#         'id' : 5,
#         'name' : 'Şirin portağal ağacım',
#         'author' : 'Joze Mauru di Vaskonselos',
#         'price' : 10,
#         'quantity': 2,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : '“Yalnız uşaqlar nə axtardıqlarını bilirlər”, – deyirdi Eqzüperi. Biz bu həqiqəti “Şirin portağal ağacım”da balaca Zezenin timsalında görürük. Zeze kasıb bir ailənin dəcəl uşağı olsa da, qəlbi günəş kimi parlaq və insan sevgisiylə doludur.',
#         'image' : 'book5.jpeg'

#     },


#     6 : {
#         'id' : 6,
#         'name' : 'Tələbə',
#         'author' : 'Tara Uestover',
#         'price' : 3.85,
#         'quantity': 3,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Libraff',
#         'description' : ' The story is about a Tələbə',
#         'image' : 'book6.jpeg'

#     },


#     7 : {
#         'id' : 7,
#         'name' : 'Stephen King',
#         'author' : 'Stephen Edwin King',
#         'price' : 15.99,
#         'quantity': 4,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Amazon',
#         'description' : 'Stephen Edwin King is an American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels.',
#         'image' : 'book7.jpeg'
#     },

    

#     8 :  {
#         'id' : 8,
#         'name' : 'Dr. Watson',
#         'author' : 'Sherlock Holmes',
#         'price' : 26.67,
#         'quantity': 2,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Libraff',
#         'description' : "Watson, in full Dr. John H. Watson, fictional English physician who is Sherlock Holmes's devoted friend and associate in a series of detective stories and novels by Sir Arthur Conan Doyle",
#         'image' : 'book8.jpeg'
#     },



#     9 : {
#         'id' : 9,
#         'name' : '1000 Words: STEM',
#         'author' : 'Jules Pottle',
#         'price' : 2.88,
#         'quantity': 1,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : "This picture word ebook of 1000 first science words is the perfect STEM ebook for helping children learn. It introduces key scientific concepts while broadening children's vocabulary and strengthening their early reading and writing skills.",
#         'image' : 'book9.jpeg'

#     },

    
#     10 : {
#         'id' : 10,
#         'name' : '101 Soruda Kuantum',
#         'author' : 'Kenneth W. Ford',
#         'price' : 7.99,
#         'quantity': 1,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'TEAS press',
#         'description' : 'Uzman bir fizikçi olan K. W. Ford, dikkatlice seçilmiş 101 sorunun cevabını herkesin anlayabileceği bir şekilde vererek, kuantum kuramının üzerindeki gizemi kaldırmayı amaçlıyor. Son yıllarda çok sık rastladığımız yanlış kuantum önyargılarını bu 101 soru-cevap ile çürütüyor. Kuantum fiziğinin en temel özelliklerinin birer özetinin yer aldığı kitap, kuantum konusunda bilmeniz gereken her şeyi özetliyor.',
#         'image' : 'book10.jpeg'

#     },


#     11 : {
#         'id' : 11,
#         'name' : '21.Yüzyıl için 21 Ders',
#         'author' : 'Yuval Noah Harari',
#         'price' : 6.99,
#         'quantity': 5,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Amazon',
#         'description' : '21. yüzyılın en çok ses getiren düşünürlerinden Yuval Noah Harari, ilk kitabı Sapiens’te insanın nasıl önemsiz bir hayvandan dünyanın efendisine dönüştüğünü, ikinci kitabı Homo Deus’ta çarpıcı öngörüleriyle insanlığın ölümsüzlük, mutluluk ve tanrısallık peşindeki yolculuğunu ele almıştı.',
#         'image' : 'book11.jpeg'

#     },


#     12 : {
#         'id' : 12,
#         'name' : 'A Maigret Christmas And Other Stories',
#         'author' : 'Georges Simenon',
#         'price' : 4.88,
#         'quantity': 3,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Kitabyurdu.com',
#         'description' : "It is Christmas in Paris, but beneath the sparkling lights and glittering decorations lie sinister deeds and dark secrets... This collection brings together three of Simenon's most enjoyable Christmas tales, newly translated, featuring Inspector Maigret and other characters from Simenon's Paris.",
#         'image' : 'book12.jpeg'

#     }

# }





# reviews = {
#     1: {'id' : 1,
#         'review_1' : 'This book is really fantastic!!!!!',
#         'review_2': 'The book has interesting content. I would recommend for all readers!!!'
#     }
# }





# bestsellers = {
#     1 : {
#         'id' : 1,
#         'name' : 'Kim deyir ki, bacarmazsan?!',
#         'author' : 'Deniel Çidiak',
#         'price' : 5.99,
#         'quantity': 3,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'TEAS press',
#         'description' : 'Deniel Çidiak bir gün öz həqiqətini yaşamadığını dərk edib və həmin gün onun həyatının dönüş nöqtəsi olub. İşindən yarımır, başqaları ilə münasibətlərindən əziyyət çəkirmiş. Gerçək dəyərləri ilə səsləşməyən seçimləri onun həyatını ağırlaşdırırmış. Lakin o, içində yatan, – və əslində hamımıza xas olan, – gizli potensialını dərk edə bilmirmiş. Beləcə, öz daxili aləminə böyük səyahətə başlayıb. ',
#         'image' : 'book1.jpeg'
#     },


#     2 :  {
#         'id' : 2,
#         'name' : 'Kürk Mantolu Madonna',
#         'author' : 'Sebahattin Ali',
#         'price' : 3.66,
#         'quantity': 2,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : "Kürk Mantolu Madonna, Sabahattin Ali'nin 1943 yılında yayımladığı bir romanıdır. Kitapta dokunaklı bir aşk hikâyesi anlatılmaktadır.",
#         'image' : 'book2.jpeg'
#     },


#     3 : {
#         'id' : 3,
#         'name' : 'Sən həyatını yaxşılaşdıra bilərsən',
#         'author' : 'Luiza Hey',
#         'price' : 20.99,
#         'quantity': 1,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : 'Əgər siz "Sən həyatını yaxşılaşdıra bilərsən" kitabında verilən çalışmaları qarşınıza çıxdıqca yerinə yetirsəniz, kitabı hələ oxuyub qurtarmamış həyatınızı dəyişməyə başlayacaqsınız. Tövsiyə edirəm ki, kitabı bir dəfə nəzərdən keçirəndən sonra onu yenidən diqqətlə oxuyasınız, lakin bu dəfə hər bir çalışmanı dostunuzla və ya ailə üzvlərinizdən biri ilə tələb olunduğu kimi yerinə yetirin. Bilin ki, bu kitabdakıları yerinə yetirərkən mənim sevgimi həmişə hiss edəcəksiniz. Luiza Hey',
#         'image' : 'book3.jpeg'

#     },

    
#     4 : {
#         'id' : 4,
#         'name' : 'Abşeron yarımadamı',
#         'author' : 'Ramil Əhməd',
#         'price' : 6.99,
#         'quantity': 1,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Libraff',
#         'description' : 'Kitabın redaktoru Aqşin Yeniseydir. Kitab yaxın günlərdə ictimaiyyətə təqdim ediləcək. Qeyd edək ki, “Abşeron yarımadamı” müəllifin beşinci kitabıdır.',
#         'image' : 'book4.jpeg'
#     },


#     5 : {
#         'id' : 5,
#         'name' : 'Şirin portağal ağacım',
#         'author' : 'Joze Mauru di Vaskonselos',
#         'price' : 10,
#         'quantity': 2,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Ali Nino',
#         'description' : '“Yalnız uşaqlar nə axtardıqlarını bilirlər”, – deyirdi Eqzüperi. Biz bu həqiqəti “Şirin portağal ağacım”da balaca Zezenin timsalında görürük. Zeze kasıb bir ailənin dəcəl uşağı olsa da, qəlbi günəş kimi parlaq və insan sevgisiylə doludur.',
#         'image' : 'book5.jpeg'

#     },


#     6 : {
#         'id' : 6,
#         'name' : 'Tələbə',
#         'author' : 'Tara Uestover',
#         'price' : 3.85,
#         'quantity': 3,
#         'currency' : ' €',
#         'availability' : 'In Stock',
#         'condition' : 'New',
#         'brand' : 'Libraff',
#         'description' : ' The story is about a Tələbə',
#         'image' : 'book6.jpeg'

#     }
# }




@app.route('/')
def home_page():
    books=Book.query.all()
    gen = Genre.query.all()
    return render_template('index.html', books=books, gen=gen)



@app.route('/products')
def products_():
    pro = Book.query.all()
    genr = Genre.query.all()
    return render_template('product.html', pro=pro, genr=genr)



@app.route('/layout')
def layouts():
    return render_template('layout.html')



@app.route('/book/<int:id>', methods=['GET', 'POST'])
def books(id):
    print(id)
    book_list = Book.query.all()
    langs = Language.query.all()
    book = Book.query.filter_by(id=id).first()
    gen = Genre.query.all()
    form = ReviewForm()
    print('post')
    if request.method == 'POST':
        form = ReviewForm(request.form)
        print(request.form)
        if form.validate_on_submit():
            print('valid')
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data,
                book_id = book.id
            )
            contact.save()
            

    contacts=Contact.query.all()
    return render_template('book.html', book=book, book_list=book_list, langs=langs, gen=gen, form = form, contacts=contacts)





@app.route('/login')
def login_page():
    return render_template('login.html')

