## eks.tf
resource "aws_eks_cluster" "eks_cluster" {
  name = var.eks_cluster_name
  role_arn = aws_iam_role.eks_role.arn
  vpc_config { subnet_ids = concat(aws_subnet.public_subnets[*].id, aws_subnet.private_subnets[*].id) }
}

resource "aws_eks_node_group" "eks_nodes" {
  cluster_name = aws_eks_cluster.eks_cluster.name
  node_role_arn = aws_iam_role.eks_node_role.arn
  subnet_ids = aws_subnet.private_subnets[*].id
  instance_types = [var.node_instance_type]
  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }
}
