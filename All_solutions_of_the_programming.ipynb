#Here are the two main issues found in the code:
#Structural Bug: Batch Size Mismatch in Discriminator Output:
#When changing the batch size from 32 to 64, you will encounter a structural bug related to the size of the output tensor from the discriminator.
#To fix this, you need to ensure that the output tensor size matches the size of all_samples_labels by modifying the discriminator output layer.
#Cosmetic Bug: Incorrect Discriminator Output Labeling:
#There is a cosmetic bug where the labels for the generated samples in the discriminator training step are incorrectly set to real_samples_labels.
#This should be corrected to generated_samples_labels to ensure proper training.
# Inside the Discriminator class, modify the output layer to match the size.

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(28 * 28, 1024),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(256, 1),  # Output layer size changed to 1
            nn.Sigmoid()
        )

# Inside the training loop, fix the label for generated samples
for epoch in range(num_epochs):
    for n, (real_samples, mnist_labels) in enumerate(train_loader):

        # Training the generator
        generator.zero_grad()
        generated_samples = generator(latent_space_samples)
        output_discriminator_generated = discriminator(generated_samples)
        
        # Fix: Use generated_samples_labels for generator training
        loss_generator = loss_function(output_discriminator_generated, generated_samples_labels)
        
        loss_generator.backward()
        optimizer_generator.step()
