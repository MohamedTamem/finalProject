#Test
# Test case one
نقوم بفحص هل يتم تخزين المنتج 
باستخدام دالة 
$response->assertStatus(200);
التي تفحص رقم حالة الاستجابة
:الكود
   public function test_store_product()
    {
        $response = $this->post('invoice');

        $response->assertStatus(200);
    }


# Test case two

نقوم بفحص هل يتم تخزين فاتورة
باستخدام دالة 
$response->assertStatus(200);
التي تفحص رقم حالة الاستجابة
:الكود

   public function test_store_invoice()
    {
        $response = $this->post('invoice');

        $response->assertStatus(200);
    }
# Test case three
نقوم بفحص هل يتم التحويل الى صفحة الفواتير
باستخدام دالة 
$response->assertStatus(200);
التي تفحص رقم حالة الاستجابة
:الكود
  public function test_index_invoice()
    {
        $response = $this->get('/all-invoice');

        $response->assertStatus(200);
    }
# Test case four
نقوم بفحص هل يتم التحويل الى صفحةالمنتجات
باستخدام دالة 
$response->assertStatus(200);
التي تفحص رقم حالة الاستجابة
:الكود
public function test_index_product()
    {
        $response = $this->get('product');

        $response->assertStatus(200);
    }
# Test case five
نقوم بفحص هل يتم تخزين الطلب الجديد
باستخدام دالة 
$response->assertStatus(200);
التي تفحص رقم حالة الاستجابة
:الكود
 public function test_store_new_order()
    {
        $response = $this->post('/new-order');

        $response->assertStatus(200);
    }
# Secound Test



 



  

    
    
   