#Temel kazanımlar

#1. Bir modülü bir bütün olarak içe aktarmak istiyorsanız, import module_name ifadesini kullanarak yapabilirsiniz. Virgülle ayrılmış bir liste kullanarak birden fazla modülü aynı anda içe aktarmanıza (import) izin verilir. Örnek:

import mod1
import mod2, mod3, mod4


#İkinci form, üslup nedenlerden dolayı önerilmemesine rağmen, aynı niyeti daha ayrıntılı ve açık bir biçimde ifade etmek daha iyi ve daha güzel:

import mod2
import mod3
import mod4


#2. Bir modül yukarıdaki şekilde içe aktarılırsa ve varlıklarından herhangi birine erişmek istiyorsanız nokta gösterimini kullanarak varlığın adını örneklendirmeniz gerekir. Örnek:

import my_module

result = my_module.my_function(my_module.my_data)


#Parçacık, my_module üzerinden gelen iki parçacığı kullanır. Bir fonksiyon olan my_function() ve bir değişken my_data. Her iki isim tarafından önek olmalıdır my_module. İçe aktarılan varlık adlarının hiçbiri,kodunuzun namespace'inde bulunan aynı adlarla çakışmaz.


#3. Bir modülü yalnızca bir bütün olarak içe aktarmanıza değil, aynı zamanda yalnızca tek varlıkları içe aktarmanıza da izin verilir. Bu durumda, içe aktarılan varlıklar, kullanıldıklarında, öneki olmamalıdır. Örnek:

from module import my_function, my_data

result = my_function(my_data)


#Yukarıdaki yol - çekiciliğine rağmen - kodun ad alanını içe aktarmaktan türetilen isimlerle çatışmalara neden olma tehlikesi nedeniyle önerilmez.


#4. Yukarıdaki ifadenin en genel formu, bir modül tarafından sunulan tüm varlıkları içe aktarmanızı sağlar:

from my_module import *

result = my_function(my_data)


#Not: Bu içe aktarma varyantı, önceden olduğu gibi aynı nedenlerden dolayı önerilmez (burada adlandırma çakışması tehdidi daha da tehlikelidir).

#5. İçe aktarılan varlığın adını “anında” kullanarak değiştirebilirsiniz. as ifadesi import'yi böyle kontrol edebiliriz. Örnek:

from module import my_function as fun, my_data as dat

result = fun(dat)



#Alıştırma 1

#Diyelim ki make_money() fonksiyonunu mint. modülü üzerinden çağırmak istiyorsunuz Kodunuz aşağıdaki satırla başlar:

import mint


#Fonksiyonun çağrılmasının uygun şekli nedir?

#Kontrol Edin
mint.make_money()



#Alıştırma 2

#Diyelim ki make_money() fonksiyonunu mint. modülü üzerinden çağırmak istiyorsunuz Kodunuz aşağıdaki satırla başlar:

from mint import make_money
	

#Fonksiyonun çağrılmasının uygun şekli nedir?

#Kontrol Edin
make_money()



#Alıştırma 3

#Peki, make_money Adında bir işlev yazdınız. Aynı adı taşıyan bir işlevi çağırmak için mint modülünü kullanın ve önceden tanımlanmış adlarınızdan hiçbirini yeniden adlandırmadan . import deyiminin hangi varyantı bu konuda size yardımcı olabilir?

#Kontrol Edin
# sample solution
from mint import make_money as make_more_money



#Alıştırma 4

#. make_money fonksiyon çağırma kodunuz aşağıdaki satırla başlıyorsa geçerlidir?

from mint import *


#Kontrol Et
make_money()



