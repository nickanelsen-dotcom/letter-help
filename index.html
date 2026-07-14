<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paper Trail Assistant - Financial Disputes</title>
    <script src="https://tailwindcss.com"></script>
</head>
<body class="bg-[#0f172a] text-[#f8fafc] min-h-screen flex flex-col items-center justify-center p-4 font-sans">
    
    <!-- Main Card Container -->
    <div class="max-w-2xl w-full bg-[#1e293b] border border-[#334155] rounded-2xl p-6 shadow-2xl space-y-6">
        <div class="text-center">
            <span class="text-xs font-semibold tracking-widest text-[#38bdf8] uppercase">AI Financial Advocate</span>
            <h1 class="text-3xl font-bold text-[#f1f5f9] mt-1">The Paper Trail Assistant</h1>
            <p class="text-sm text-[#94a3b8] mt-1">Generate professional dispute letters for insurance, payroll, and hidden fees instantly.</p>
        </div>
        
        <div class="space-y-2">
            <label class="block text-sm font-semibold text-[#cbd5e1]">1. Select Your Dispute Type</label>
            <select id="dispute-type" class="w-full bg-[#0f172a] border border-[#334155] rounded-xl p-3 text-[#f8fafc] focus:outline-none focus:border-[#38bdf8]">
                <option value="insurance">Insurance Policy / Cancelled Benefits Dispute</option>
                <option value="payroll">Payroll / Unauthorized Union Deduction Dispute</option>
                <option value="subscription">Subscription Overcharge / Price Hike Dispute</option>
            </select>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="space-y-1">
                <label class="block text-xs font-medium text-[#94a3b8]">Your Full Name</label>
                <input id="user-name" type="text" placeholder="John Doe" class="w-full bg-[#0f172a] border border-[#334155] rounded-xl p-3 text-[#f8fafc] text-sm focus:outline-none focus:border-[#38bdf8]">
            </div>
            <div class="space-y-1">
                <label class="block text-xs font-medium text-[#94a3b8]">Company / Entity Name</label>
                
            </div>
            <div class="space-y-1">
                <label class="block text-xs font-medium text-[#94a3b8]">Policy or Account Number</label>
                <input id="account-id" type="text" placeholder="POL-123456 / ACC-789" class="w-full bg-[#0f172a] border border-[#334155] rounded-xl p-3 text-[#f8fafc] text-sm focus:outline-none focus:border-[#38bdf8]">
            </div>
            <div class="space-y-1">
                <label class="block text-xs font-medium text-[#94a3b8]">Disputed Amount ($)</label>
                <input id="dispute-amount" type="number" placeholder="500.00" class="w-full bg-[#0f172a] border border-[#334155] rounded-xl p-3 text-[#f8fafc] text-sm focus:outline-none focus:border-[#38bdf8]">
            </div>
        </div>
        
        <button onclick="generateLetterFromInputs()" class="w-full py-3.5 bg-[#38bdf8] hover:bg-[#0ea5e9] text-[#0f172a] font-bold rounded-xl transition duration-200 shadow-md">
            Draft AI Dispute Letter
        </button>
        
        <div id="output-section" class="hidden space-y-4 pt-4 border-t border-[#334155]">
            <h3 class="text-sm font-semibold text-[#38bdf8] uppercase tracking-wider">Generated Document Preview</h3>
            <div id="letter-body" class="whitespace-pre-wrap font-mono text-xs bg-[#0f172a] p-5 rounded-xl border border-[#334155] text-[#cbd5e1] leading-relaxed max-h-64 overflow-y-auto"></div>
            <div class="bg-[#1e293b] border border-[#0284c7] p-4 rounded-xl flex flex-col md:flex-row items-center justify-between gap-4">
                <div>
                    <h4 class="text-sm font-bold text-[#f1f5f9]">Need the Official, Certified Version?</h4>
                    <p class="text-xs text-[#94a3b8]">Unlock PDF download formats and automatic legal formatting templates.</p>
                </div>
                <button onclick="triggerPaywall()" class="w-full md:w-auto px-6 py-2.5 bg-[#22c55e] hover:bg-[#16a34a] text-white font-semibold rounded-xl text-sm transition duration-200 shadow">
                    Download Certified Document ($5)
                </button>
            </div>
        </div>

        <!-- Compliance Layout Footer -->
        <div class="pt-6 border-t border-[#334155] text-center space-y-3">
            <p class="text-[10px] text-[#64748b] leading-relaxed">
                Disclaimer: The Paper Trail Assistant provides automated self-help templates. We are not attorneys or financial advisors. This software does not constitute formal legal or financial representation.
            </p>
            <div class="flex justify-center space-x-4 text-xs text-[#38bdf8]">
                <button onclick="openModal('privacy')" class="hover:underline">Privacy Policy</button>
                <button onclick="openModal('terms')" class="hover:underline">Terms of Service</button>
                <button onclick="openModal('refund')" class="hover:underline">Refund Policy</button>
            </div>
            <p class="text-xs text-[#94a3b8]">Contact Support: support@yourdomain.com</p>
        </div>
    </div>

    <!-- Legal Policy Popup Modal -->
    <div id="policy-modal" class="hidden fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
        <div class="bg-[#1e293b] border border-[#334155] max-w-lg w-full max-h-[80vh] rounded-2xl p-6 flex flex-col space-y-4">
            <h2 id="modal-title" class="text-xl font-bold text-[#38bdf8]"></h2>
            <div id="modal-content" class="overflow-y-auto font-mono text-xs text-[#cbd5e1] bg-[#0f172a] p-4 rounded-xl leading-relaxed whitespace-pre-wrap flex-1"></div>
            <button onclick="closeModal()" class="w-full py-2 bg-[#334155] hover:bg-[#475569] text-white font-semibold rounded-xl transition">Close</button>
        </div>
    </div>

    <script>
        function openModal(type) {
            let title = "";
            let text = "";
            
            if (type === 'privacy') {
                title = "Privacy Policy";
                text = "We value your privacy. The data inputted into this form is processed strictly in your local web browser engine to compile templates. We do not transmit, log, store, or sell any information typed into our dispute generator. Payments are handled externally via Stripe.";
            } else if (type === 'terms') {
                title = "Terms of Service";
                text = "By using Paper Trail Assistant, you explicitly acknowledge that you are selecting self-service digital templates. This utility does not guarantee legal outcome, financial settlement, or institutional response. Users are solely responsible for verifying facts before sending.";
            } else if (type === 'refund') {
                title = "Refund & Fulfillment Policy";
                text = "Due to the immediate digital asset deployment of our documentation packages, all sales ($5.00) are final. If a technical error prevents your download link from firing, reach out to support@yourdomain.com.";
            }
            
            document.getElementById('modal-title').innerText = title;
            document.getElementById('modal-content').innerText = text;
            document.getElementById('policy-modal').classList.remove('hidden');
        }
        
        function closeModal() { 
            document.getElementById('policy-modal').classList.add('hidden'); 
        }

        function generateLetterFromInputs() {
            const type = document.getElementById('dispute-type').value;
            const name = document.getElementById('user-name').value || "[Your Name]";
            const entity = document.getElementById('entity-name').value || "[Company Name]";
            const id = document.getElementById('account-id').value || "[ID/Account Number]";
            const amount = document.getElementById('dispute-amount').value || "0.00";
            
            let letterText = "";
            
            if (type === 'insurance') {
                letterText = "TO: Claims Department\nFROM: " + name + "\nRE: Insurance Dispute\nPolicy ID: " + id + "\n\nDear Team,\n\nI am writing to dispute charges or cancellations regarding my coverage with " + entity + ". Records indicate that funds totaling $" + amount + " have been remitted, yet benefits have been restricted without notice.\n\nSincerely,\n" + name;
            } else if (type === 'payroll') {
                letterText = "TO: Payroll Department\nFROM: " + name + "\nRE: Unauthorized Payroll Deduction Notice\nEmployee ID: " + id + "\n\nDear Administrator,\n\nThis serves as notice that an unauthorized deduction of $" + amount + " has been taken from my wages on behalf of " + entity + ".\n\nSincerely,\n" + name;
            } else if (type === 'subscription') {
                letterText = "TO: Billing Department\nFROM: " + name + "\nRE: Unfair Pricing Increase Dispute\nAccount ID: " + id + "\n\nTo Whom It May Concern,\n\nI object to the recent pricing adjustment on my account with " + entity + ", which resulted in an overcharge of $" + amount + ".\n\nSincerely,\n" + name;
            }
            
            document.getElementById('letter-body').innerText = letterText;
            document.getElementById('output-section').classList.remove('hidden');
        }

        function triggerPaywall() {
            // Replace the URL inside these quotes with your actual Stripe Payment Link
            window.location.href = "https://buy.stripe.com/test_bJeaEW3NocdSfsGf4Y5Vu00";
        }
    </script>
</body>
</html>
